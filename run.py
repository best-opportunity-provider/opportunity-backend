import random
import json
import time
import asyncio
from typing import Any

from scrapers import html_opportunity, get_opportunity_links
from opportunity_misc.transformer.queries import query_opportunity
from opportunity_misc.transformer.config import client
from opportunity_misc.ai_translator.translators import translate_opportunity

REQUESTS_PER_MINUTE = 8 

async def process_single_opportunity(
        url: str, 
        output_folder: str | None = None,
    ) -> dict[str, Any]:
    opportunity = await asyncio.to_thread(html_opportunity, url)
    if opportunity == None:
        return
    query_output = await query_opportunity(
        client,
        opportunity['main_html'],
        opportunity['form_html'],
        opportunity['url'],
        'opportunity_misc\\transformer\\outputs\\all'
    )
    translate_output = await translate_opportunity(
        query_output,
        opportunity['url']
    )

    if output_folder is not None:
        with open(f'{output_folder}\\{hash(url)}.json', 'w', encoding='utf-8') as f:
            json.dump(translate_output, f, indent=4)
            f.close()
    return translate_output

async def process_opportunities(
        links: list[str], 
        output_folder: str | None = None,
        visible_work_time: bool = False, 
    ) -> list[dict[str, Any]]:
    if not links:
        return []

    start_time = time.time()
    tasks = []
    
    # Запускаем задачи с интервалом 7.5 секунд (8 задач/минуту)
    for url in links:
        task = asyncio.create_task(process_single_opportunity(url, output_folder))
        tasks.append(task)
        await asyncio.sleep(60 / REQUESTS_PER_MINUTE)
    
    result = await asyncio.gather(*tasks)
    
    if visible_work_time:
        total_time = time.time() - start_time
        hours = int(total_time // 3600)
        minutes = int(total_time % 3600 // 60)
        seconds = int(total_time % 60)
        print(f"--- All work time: {hours:02}h {minutes:02}m {seconds:02}s ---")

    return result

if __name__ == "__main__":
    filename = 'links.txt'
    # get_opportunity_links(filename)
    links = []
    with open(filename, mode='r') as file:
        for line in file:
            link = line.strip()
            if link:
                links.append(link)
    asyncio.run(process_opportunities(random.sample(links, k=10), 'outputs', True))
    print('End')
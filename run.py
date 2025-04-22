from scrapers import parse_opportunity
from opportunity_misc.transformer.queries import query_opportunity
from opportunity_misc.transformer.config import client
from opportunity_misc.ai_translator.translators import translate_opportunity
import time
from typing import Dict, Any
import asyncio
import json

async def start_pipeline(links: list[str], visible_work_time: bool = False) -> None:
    start_time = time.time()
    opportunitys = []
    for url in links:
        start_opportunity_time = time.time()
        opportunity = parse_opportunity(url)
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
        opportunitys.append(translate_output)
        
        with open('test.json', 'a', encoding='utf-8') as f:
            json.dump(translate_output, f, ensure_ascii=False, indent=4)
            f.write('\n')
        
        opportunity_time = start_opportunity_time - time.time()
        time.sleep((15 - opportunity_time) if opportunity_time < 15 else 0)
            
    if visible_work_time:
        print(f"--- AllWebParse work time: {(int(time.time() - start_time) // 3600):2}h {(int(time.time() - start_time) % 3600 // 60):2}m {(int(time.time() - start_time) % 60):2}s ---")

if __name__ == "__main__":
    asyncio.run(
        start_pipeline(
            ['https://yandex.ru/jobs/vacancies/team-lead-mb-v-reklamu-20269'],
            True
        )
    )

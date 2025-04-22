from ..config import *

def run(vacancy_link: str) -> CategorizedOpportunityDump:
    driver.get(vacancy_link)
    html = BeautifulSoup(driver.page_source, "html.parser")
    html_code = str(html.find("main", class_="flex flex-col text-neutral-800"))
    form_code = None

    try:
        form_url = html.find("div", class_="flex items-center gap-2 text-[10px] xs:text-xs md:gap-4 md:text-sm").find_all('a')[1].get('href')
        driver.get(form_url)
        sleep(2)
        html = BeautifulSoup(driver.page_source, "html.parser")
        form_code = str(html.find('div', class_='frm_fields_container'))
    except Exception as e:
        print(f"An error occurred: {e}\n")

    vacancy = CategorizedOpportunityDump(
                                        url= vacancy_link, 
                                        main_html= html_code, 
                                        form_html= form_code)
    
    return vacancy  

# t = get_goabroad_opportunity_dump('https://www.goabroad.com/providers/aifs-abroad/programs/study-abroad-discover-world-aifs!-170052')
# with open('tmp.json', 'w') as f:
#     json.dump(t, f)
    
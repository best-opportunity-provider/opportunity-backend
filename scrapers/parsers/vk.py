from ..config import *

def run(vacancy_link: str) -> CategorizedOpportunityDump:
    driver.get(vacancy_link)
    html = BeautifulSoup(driver.page_source, "html.parser")

    html_code = str(html.find("main"))
    form_code = None
    if '<div class=\"VACANCY_APPLICATION_CLASSNAME next-7mfv7y\">' in html_code:
        form_code = html_code[html_code.find('<div class=\"VACANCY_APPLICATION_CLASSNAME next-7mfv7y\">'):]

    vacancy = CategorizedOpportunityDump(
                                        url= vacancy_link, 
                                        main_html= html_code, 
                                        form_html= form_code)
    
    return vacancy  

def get_links(link_driver, filename) -> None:
    try:
        link_driver.get('https://internship.vk.company/vacancy')
        elems = link_driver.find_elements(By.CLASS_NAME, 'CommandsCard  next-4mx6ez')
        with open(filename, 'a', encoding='utf-8') as f:
                for elem in elems:
                    f.write(f'https://internship.vk.company{elem.get_attribute("href")}\n')
        link_driver.close()
    except Exception as e:
        print(f"Error in get_links_vk: {str(e)}")

# t = get_vk_opportunity_dump('https://internship.vk.company/vacancy/1092')
# with open('tmp.json', 'w') as f:
#     json.dump(t, f)
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

# t = get_vk_opportunity_dump('https://internship.vk.company/vacancy/1092')
# with open('tmp.json', 'w') as f:
#     json.dump(t, f)
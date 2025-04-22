from ..config import *

def run(vacancy_link: str) -> CategorizedOpportunityDump:
    driver.get(vacancy_link)
    html = BeautifulSoup(driver.page_source, "html.parser")

    html_code = str(html.find("div", class_="container-xl mt-sm-3"))
    form_code = html.find("div", id='collapse-portable-concierge-form')
    if form_code:
        form_code = str(form_code)

    vacancy = CategorizedOpportunityDump(
                                        url=vacancy_link, 
                                        main_html= html_code, 
                                        form_html= form_code)

    return vacancy  

# t = get_inter_student_opportunity_dump('https://www.internationalstudent.com/school-search/1832/usa/georgia/brenau-university/')
# with open('tmp.json', 'w') as f:
#     json.dump(t, f)
from ..config import *

def run(vacancy_link: str) -> CategorizedOpportunityDump:
    driver.get(vacancy_link)
    html = BeautifulSoup(driver.page_source, "html.parser")

    html_code = str(html.find("div", class_="content"))
    form_code = html.find('div', class_='side__form')
    if form_code:
        form_code = str(form_code)

    vacancy = CategorizedOpportunityDump(
                                        url=vacancy_link, 
                                        main_html=html_code, 
                                        form_html=form_code)

    return vacancy  

# t = get_studyqa_opportunity_dump('https://ru.studyqa.com/internships/view/aples-hotel-internship')
# with open('tmp.json', 'w') as f:
#     json.dump(t, f)
from ..config import *

def run(vacancy_link: str) -> CategorizedOpportunityDump:
    driver.get(vacancy_link)
    html = BeautifulSoup(driver.page_source, "html.parser")
    html_code = str(html.find("div", class_="vacancy-detail__content"))
    form_code = None

    try:
        form_code = str(html.find("div", class_="vacancy-response"))
    except Exception as e:
        print(f"An error occurred: {e}\n")

    vacancy = CategorizedOpportunityDump(
                                        url= vacancy_link, 
                                        main_html= html_code, 
                                        form_html= form_code)
    
    return vacancy  

# t = get_croc_opportunity_dump('https://careers.croc.ru/vacancies/senior-frontend-razrabotchika-react/#responseForm')
# with open('tmp.json', 'w') as f:
#     json.dump(t, f)
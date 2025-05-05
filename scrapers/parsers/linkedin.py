from ..config import *

def run(vacancy_link: str) -> CategorizedOpportunityDump:
    driver.get(vacancy_link)
    html = BeautifulSoup(driver.page_source, "html.parser")

    html_code = str(html.find("div", class_="jobs-details__main-content jobs-details__main-content--single-pane full-width"))
    form_code = None

    vacancy = CategorizedOpportunityDump(
                                        url= vacancy_link, 
                                        main_html= html_code, 
                                        form_html= form_code)
    
    return vacancy  

def get_links(link_driver, filename) -> None:
    try:
        links = []
    except Exception as e:
        print(f"Error in get_links_linkedin: {str(e)}")

# t = get_tbank_opportunity_dump('https://www.linkedin.com/jobs/collections/recommended/?currentJobId=4190525465')
# with open('tmp.json', 'w') as f:
#     json.dump(t, f)
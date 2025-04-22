from ..config import *

def run(vacancy_link: str) -> CategorizedOpportunityDump:
    driver.get(vacancy_link)
    sleep(5)
    html_code = BeautifulSoup(driver.page_source, "html.parser")
    main_code = str(html_code.find("div", class_="DkhPwc"))
    form_code = None

    vacancy = CategorizedOpportunityDump(url=vacancy_link, 
                                         main_html=main_code, 
                                         form_html=form_code)

    return vacancy

# t = run('https://www.google.com/about/careers/applications/jobs/results/75226763403109062-microled-display-product-engineer')
# with open('tmp.json', 'w') as f:
#     json.dump(t, f)
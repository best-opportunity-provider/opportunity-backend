from ..config import *

def run(vacancy_link: str) -> CategorizedOpportunityDump:
    driver.get(vacancy_link)
    sleep(5)
    html_code = BeautifulSoup(driver.page_source, "html.parser")
    main_code = str(html_code.find("div", class_="hr_vacancy__tXHW_ mt-8 mt-xs-4"))
    form_code = html_code.find('div', class_="hr_form__t15hw hr_section__xE2of")
    
    if form_code:
        form_code = str(form_code)


    vacancy = CategorizedOpportunityDump(url=vacancy_link, 
                                         main_html=main_code, 
                                         form_html=form_code)

    return vacancy

# t = run('https://tochka.com/hr/it/technical-product-manager/')
# with open('tmp.json', 'w') as f:
#     json.dump(t, f)
from ..config import *

def run(vacancy_link: str) -> CategorizedOpportunityDump:
    driver.get(vacancy_link)
    html = BeautifulSoup(driver.page_source, "html.parser")
    html_code = str(html.find("div", class_="MuiStack-root mui-1ov46kg"))
    form_code = None
    
    try:
        dom = etree.HTML(driver.page_source)
        tree = etree.ElementTree(dom)
        buttons = dom.xpath('//*/button')
        if len(buttons) > 0:
            driver.find_element(by="xpath", value=tree.getpath(buttons[0])).click()
            sleep(2)
            html = BeautifulSoup(driver.page_source, "html.parser")
            html_code = str(html.find("div", class_="MuiStack-root mui-1ov46kg"))
            form_code = str(html.find('div', class_='VacancyResponseForm_formContainer__LWKxP MuiBox-root mui-1nb1l1t'))
    except Exception as e:
        print(f"An error occurred: {e}")

    vacancy = CategorizedOpportunityDump(url= vacancy_link, 
                                         main_html= html_code, 
                                         form_html= form_code)
    
    return vacancy  

# t = get_superjob_opportunity_dump('https://students.superjob.ru/stazhirovki/47102401/')
# with open('tmp.json', 'w') as f:
#     json.dump(t, f)
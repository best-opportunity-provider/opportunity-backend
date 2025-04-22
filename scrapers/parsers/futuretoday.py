from ..config import *

def run(vacancy_link: str) -> CategorizedOpportunityDump:
    driver.get(vacancy_link)
    html = BeautifulSoup(driver.page_source, "html.parser")
    sleep(2)
    html_code = str(html.find("div", id="__next"))
    form_code = None
    try:
        dom = etree.HTML(driver.page_source)
        tree = etree.ElementTree(dom)
        buttons = dom.xpath('//*/section/button')
        if len(buttons) > 0:
            driver.find_element(by="xpath", value=tree.getpath(buttons[0])).click()
            sleep(2)
            html = BeautifulSoup(driver.page_source, "html.parser")
            html_code = str(html.find("div", id="__next"))
            form_code = str(html.find('div', class_='sc-gKsecS hHWvTk'))
    except Exception as e:
        print(f"An error occurred: {e}\n")

    vacancy = CategorizedOpportunityDump(
                                        url= vacancy_link, 
                                        main_html= html_code, 
                                        form_html= form_code)
    
    return vacancy  

# t = get_futuretoday_opportunity_dump('https://fut.ru/internship/fbk/probation?utm_source=fut&utm_medium=catalog')
# with open('tmp.json', 'w') as f:
#     json.dump(t, f)

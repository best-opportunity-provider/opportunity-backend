from ..config import *
from selenium.common.exceptions import NoSuchElementException

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

def get_links(link_driver, filename) -> None:
    try:
        link_driver.get('https://fut.ru/')
        while True:
            link_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(2)
            try:
                next_but = link_driver.find_element(By.CLASS_NAME, 'sc-fWSCoS kdKWuP')
                next_but.click()
            except NoSuchElementException:
                break
        elems = link_driver.find_elements(By.CLASS_NAME, 'sc-Tmeag sc-kiYrGK xYdWi leTVnx')
        with open(filename, 'a', encoding='utf-8') as f:
            for elem in elems:
                f.write(f'https://fut.ru{elem.get_attribute("href")}\n')
        link_driver.close()
    except Exception as e:
        print(f"Error in get_links_futuretoday: {str(e)}")

# t = get_futuretoday_opportunity_dump('https://fut.ru/internship/fbk/probation?utm_source=fut&utm_medium=catalog')
# with open('tmp.json', 'w') as f:
#     json.dump(t, f)

from ..config import *

def run(vacancy_link: str) -> CategorizedOpportunityDump:
    driver.get(vacancy_link)
    html = BeautifulSoup(driver.page_source, "html.parser")

    html_code = str(html.find("div", class_="application"))
    form_code = html.find("div",class_="gbzPLTeEC")
    if form_code:
        form_code = str(form_code)

    vacancy = CategorizedOpportunityDump(
                                        url= vacancy_link, 
                                        main_html= html_code, 
                                        form_html= form_code)
    
    return vacancy  

def get_links(link_driver, filename) -> None:
    try:
        link_driver.get('https://education.tbank.ru/start/')
        for but in link_driver.find_elements(By.CLASS_NAME, 'jb8T3OHMg'):
            but.click()
            sleep(1)
        elems = link_driver.find_elements(By.CLASS_NAME, 'fbKdZAZDB')
        link_driver.close()
        with open(filename, 'a', encoding='utf-8') as f:
            for elem in elems:
                f.write(f'https://education.tbank.ru{elem.get_attribute("href")}\n')
    except Exception as e:
        print(f"Error in get_links_tbank: {str(e)}")

# t = get_tbank_opportunity_dump('https://education.tbank.ru/start/java/')
# with open('tmp.json', 'w') as f:
#     json.dump(t, f)
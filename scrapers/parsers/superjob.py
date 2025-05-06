from ..config import *

def run(vacancy_link: str) -> CategorizedOpportunityDump:
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_page_load_timeout(30)
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

def get_links(link_driver, filename) -> None:
    try:
        links = []
        num_page = 1
        while(True):
            link_driver.get(f'https://students.superjob.ru/vakansii/?page={num_page}')
            sleep(2)
            elems = link_driver.find_elements(By.CLASS_NAME, "VacancySnippet_link__sF_cO")
            if not elems:
                break
            with open(filename, 'a', encoding='utf-8') as f:
                for elem in elems:
                    f.write(f'{elem.get_attribute("href")}\n')
            num_page += 1
        link_driver.close()
    except Exception as e:
        print(f"Error in get_links_superjob: {str(e)}")

# t = get_superjob_opportunity_dump('https://students.superjob.ru/stazhirovki/47102401/')
# with open('tmp.json', 'w') as f:
#     json.dump(t, f)
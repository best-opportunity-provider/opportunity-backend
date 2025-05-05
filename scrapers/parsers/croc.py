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

def get_links(link_driver, filename) -> None:
    try:
        links = []
        num_page = 0
        while(True):
            num_page += 1
            link_driver.get(f'https://careers.croc.ru/vacancies/?sections={num_page}')
            sleep(2)
            elems = link_driver.find_elements(By.CSS_SELECTOR, "a.size-normal size-md-smaller")
            if num_page > 50:
                break
            if not elems:
                continue
            with open(filename, 'a', encoding='utf-8') as f:
                for elem in elems:
                    f.write(f'https://careers.croc.ru{elem.get_attribute("href")}\n')
        link_driver.close()
    except Exception as e:
        print(f"Error in get_links_croc: {str(e)}")

# t = get_croc_opportunity_dump('https://careers.croc.ru/vacancies/senior-frontend-razrabotchika-react/#responseForm')
# with open('tmp.json', 'w') as f:
#     json.dump(t, f)
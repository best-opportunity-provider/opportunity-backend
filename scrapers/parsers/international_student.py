from ..config import *

def run(vacancy_link: str) -> CategorizedOpportunityDump:
    driver.get(vacancy_link)
    html = BeautifulSoup(driver.page_source, "html.parser")

    html_code = str(html.find("div", class_="container-xl mt-sm-3"))
    form_code = html.find("div", id='collapse-portable-concierge-form')
    if form_code:
        form_code = str(form_code)

    vacancy = CategorizedOpportunityDump(
                                        url=vacancy_link, 
                                        main_html= html_code, 
                                        form_html= form_code)

    return vacancy  

def get_links(link_driver, filename) -> None:
    try:
        links = []
        num_page = 1
        while(True):
            link_driver.get(f'https://www.internationalstudent.com/school-search/usa/search/?page={num_page}&per-page=25')
            sleep(2)
            elems = link_driver.find_elements(By.CLASS_NAME, "font-bitter text-left text-danger mb-2 mb-lg-0")
            if not elems:
                break
            with open(filename, 'a', encoding='utf-8') as f:
                for elem in elems:
                    f.write(f'https://www.internationalstudent.com{elem.get_attribute("href")}\n')
            num_page += 1
        link_driver.close()
    except Exception as e:
        print(f"Error in get_links_internationalstudent: {str(e)}")

# t = get_inter_student_opportunity_dump('https://www.internationalstudent.com/school-search/1832/usa/georgia/brenau-university/')
# with open('tmp.json', 'w') as f:
#     json.dump(t, f)
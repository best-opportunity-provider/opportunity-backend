from ..config import *

def run(vacancy_link: str) -> CategorizedOpportunityDump:
    driver.get(vacancy_link)
    html = BeautifulSoup(driver.page_source, "html.parser")

    html_code = str(html.find("div", class_="content"))
    form_code = html.find('div', class_='side__form')
    if form_code:
        form_code = str(form_code)

    vacancy = CategorizedOpportunityDump(
                                        url=vacancy_link, 
                                        main_html=html_code, 
                                        form_html=form_code)

    return vacancy  

def get_links(link_driver, filename) -> None:
    try:
        links = []
        num_page = 1
        while(True):
            link_driver.get(f'https://ru.studyqa.com/internships/countries/cities/industries?page={num_page}')
            sleep(2)
            elems = link_driver.find_elements(By.CLASS_NAME, "btn btn-secondary")
            if not elems:
                break
            with open(filename, 'a', encoding='utf-8') as f:
                for elem in elems:
                    f.write(f'{elem.get_attribute("href")}\n')
            num_page += 1
        link_driver.close()
    except Exception as e:
        print(f"Error in get_links_studyqa: {str(e)}")

# t = get_studyqa_opportunity_dump('https://ru.studyqa.com/internships/view/aples-hotel-internship')
# with open('tmp.json', 'w') as f:
#     json.dump(t, f)
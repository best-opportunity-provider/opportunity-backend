from ..config import *

def run(vacancy_link: str) -> CategorizedOpportunityDump:
    driver.get(vacancy_link)
    sleep(1)
    html = BeautifulSoup(driver.page_source, "html.parser")

    html_code = str(html.find("div", class_="ant-card ant-card-bordered _slug__vacancy__rfuny css-q9fvyu"))
    form_code = None
    button = html.find('button', id="response-btn")
    if button:
        driver.find_element(By.ID, "response-btn").click()
        sleep(1)
        html = BeautifulSoup(driver.page_source, "html.parser")
        form_code = html.find("div", class_="ant-modal-content")

    if form_code:
        form_code = str(form_code)

    vacancy = CategorizedOpportunityDump(
                                        url= vacancy_link, 
                                        main_html= html_code, 
                                        form_html= form_code)
    
    return vacancy  

def get_links(link_driver, filename) -> None:
    try:
        links = []
        num_page = 1
        while(True):
            link_driver.get(f'https://my.jobby.ai/vacancies?page={num_page}')
            sleep(2)
            elems = link_driver.find_elements(By.CSS_SELECTOR, "a.Vacancy_container__taDiH")
            if not elems:
                break
            with open(filename, 'a', encoding='utf-8') as f:
                for elem in elems:
                    f.write(f'https://my.jobby.ai{elem.get_attribute("href")}\n')
            num_page += 1
        link_driver.close()
        return links
    except Exception as e:
        print(f"Error in get_links_jobby: {str(e)}")

# t = run('https://my.jobby.ai/vacancies/finansovyj-menedzher-7038?utm_campaign=118693420&utm_medium=cpc&utm_source=yandex&utm_term=---autotargeting.desktop.Москва.54456796932.none&utm_content=16896072631')
# with open('tmp.json', 'w') as f:
#     json.dump(t, f)
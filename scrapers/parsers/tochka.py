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

def get_links(link_driver, filename) -> None:
    try:
        link_driver.get('https://tochka.com/hr/vacancies/')
        last_height = link_driver.execute_script("return document.body.scrollHeight")
        while True:
            link_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(2)
            new_height = link_driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        elems = link_driver.find_elements(By.CSS_SELECTOR, ".jobs_jobsListItem__z2T4u a")
        with open(filename, 'a', encoding='utf-8') as f:
                for elem in elems:
                    f.write(f'{elem.get_attribute("href")}\n')
        link_driver.close()
    except Exception as e:
        print(f"Error in get_links_tochka: {str(e)}")

# t = run('https://tochka.com/hr/it/technical-product-manager/')
# with open('tmp.json', 'w') as f:
#     json.dump(t, f)
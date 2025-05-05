from ..config import *

def run(vacancy_link: str) -> CategorizedOpportunityDump:
    driver.get(vacancy_link)
    html = BeautifulSoup(driver.page_source, "html.parser")

    html_code = str(html.find("article", class_="vacancy-show"))
    
    button = html.find('a', class_='button-comp button-comp--appearance-primary button-comp--size-m')
    if button != None:
        driver.get(button.get('href'))
        try:
            wait = WebDriverWait(driver, 10)
            email = wait.until(EC.element_to_be_clickable((By.NAME, "email")))
            email.send_keys('gauterderfork@gmail.com')
            password = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
            password.send_keys('6zL-LGT-nEy-Pit')
            while driver.current_url != 'https://career.habr.com/vacancies?type=all': True
            driver.get(vacancy_link)
        except Exception as e:
            print(f"An error occurred: {e}")

    form_code = html.find('div', class_='section-box')
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
            link_driver.get(f'https://career.habr.com/vacancies?page={num_page}&type=all')
            sleep(2)
            elems = link_driver.find_elements(By.CLASS_NAME, "vacancy-card__title-link")
            if not elems:
                break
            with open(filename, 'a', encoding='utf-8') as f:
                for elem in elems:
                    f.write(f'{elem.get_attribute("href")}\n')
            num_page += 1
        link_driver.close()
    except Exception as e:
        print(f"Error in get_links_habr: {str(e)}")

# t = get_inter_student_opportunity_dump('https://career.habr.com/vacancies/1000127535')
# with open('tmp.json', 'w') as f:
#     json.dump(t, f)
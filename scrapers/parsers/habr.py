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

# t = get_inter_student_opportunity_dump('https://career.habr.com/vacancies/1000127535')
# with open('tmp.json', 'w') as f:
#     json.dump(t, f)
from ..config import *

def run(vacancy_link: str) -> CategorizedOpportunityDump:
    driver.get(vacancy_link)
    sleep(5)
    html_code = BeautifulSoup(driver.page_source, "html.parser")
    main_code = str(html_code.find("div", class_="lc-page__content"))
    form_code = None

    form_iframe = html_code.find('iframe', class_="lc-iframe__iframe")
    if form_iframe != None:
        driver.get(form_iframe.get('src').split('/?')[0])
        sleep(2)
        form_code = str(BeautifulSoup(driver.page_source, "html.parser"))


    vacancy = CategorizedOpportunityDump(url=vacancy_link, 
                                         main_html=main_code, 
                                         form_html=form_code)

    return vacancy

def get_links() -> list[str]:
    links = []
    driver.get('https://yandex.ru/jobs/vacancies')
    sleep(2)
    links = driver.find_elements(By.CLASS_NAME, 'lc-jobs-vacancy-card__link')
    return links

# t = get_yandex_opportunity_dump('https://yandex.ru/jobs/vacancies/stazhyor-v-komandu-promishlennogo-dizayna-umnih-ustroystv-s-alisoy-30267')
# with open('tmp.json', 'w') as f:
#     json.dump(t, f)
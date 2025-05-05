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

def get_links(link_driver, filename) -> None:
    try:
        print('yandex')
        link_driver.get('https://yandex.ru/jobs/vacancies')
        last_height = link_driver.execute_script("return document.body.scrollHeight")
        while True:
            link_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(1)
            now_height = link_driver.execute_script("return document.body.scrollHeight")
            if now_height >= 1900000 or abs(last_height - now_height) <= 100:
                break
            last_height = now_height
        elems = link_driver.find_elements(By.CLASS_NAME, 'lc-jobs-vacancy-card__link')
        with open(filename, 'a', encoding='utf-8') as f:
            for elem in elems:
                f.write(f'{elem.get_attribute("href")}\n')
        link_driver.close()
    except Exception as e:
        print(f"Error in get_links_yandex: {str(e)}")

# t = get_yandex_opportunity_dump('https://yandex.ru/jobs/vacancies/stazhyor-v-komandu-promishlennogo-dizayna-umnih-ustroystv-s-alisoy-30267')
# with open('tmp.json', 'w') as f:
#     json.dump(t, f)
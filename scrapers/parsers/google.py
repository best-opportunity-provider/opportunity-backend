from ..config import *

def run(vacancy_link: str) -> CategorizedOpportunityDump:
    driver.get(vacancy_link)
    sleep(5)
    html_code = BeautifulSoup(driver.page_source, "html.parser")
    main_code = str(html_code.find("div", class_="DkhPwc"))
    form_code = None

    vacancy = CategorizedOpportunityDump(url=vacancy_link, 
                                         main_html=main_code, 
                                         form_html=form_code)

    return vacancy


def get_links(link_driver, filename) -> None:
    try:
        links = []
        num_page = 1
        while(True):
            link_driver.get(f'https://www.google.com/about/careers/applications/jobs/results?page={num_page}')
            sleep(2)
            elems = link_driver.find_elements(By.CLASS_NAME, "WpHeLc VfPpkd-mRLv6 VfPpkd-RLmnJb")[1:]
            if not elems:
                break
            with open(filename, 'a', encoding='utf-8') as f:
                for elem in elems:
                    f.write(f'https://www.google.com/about/careers/applications/{elem.get_attribute("href")}\n')
            num_page += 1
        link_driver.close()
    except Exception as e:
        print(f"Error in get_links_google: {str(e)}")

# t = run('https://www.google.com/about/careers/applications/jobs/results/75226763403109062-microled-display-product-engineer')
# with open('tmp.json', 'w') as f:
#     json.dump(t, f)
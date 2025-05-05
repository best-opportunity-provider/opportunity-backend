from ..config import *

def run(vacancy_link: str) -> CategorizedOpportunityDump:
  driver.get(vacancy_link)
  html = BeautifulSoup(driver.page_source, "html.parser")
  
  html_code = str(html.find("div", class_="vacancy-without-form-wrapper"))
  form_code = html.find('div', class_='vacancy-response')
  if form_code:
    form_code = str(form_code)

  vacancy = CategorizedOpportunityDump(
                                      url= vacancy_link, 
                                      main_html= html_code, 
                                      form_html= form_code)
  return vacancy  

def get_links(link_driver, filename) -> None:
    try:
      link_driver.get('https://changellenge.com/vacancy/')
      last_height = link_driver.execute_script("return document.body.scrollHeight")
      while True:
          link_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
          sleep(1)
          now_height = link_driver.execute_script("return document.body.scrollHeight")
          if now_height >= 1900000 or abs(last_height - now_height) <= 100:
              break
          last_height = now_height
      elems = link_driver.find_elements(By.CLASS_NAME, 'new-vacancies-card__link new-vacancies-card__content-link')
      with open(filename, 'a', encoding='utf-8') as f:
          for elem in elems:
              f.write(f'https://changellenge.com{elem.get_attribute("href")}\n')
      link_driver.close()
    except Exception as e:
        print(f"Error in get_links_changellenge: {str(e)}")

# t = get_changellenge_opportunity_dump('https://changellenge.com/vacancy/frontend-development-alabuga-elabuga/')
# with open('tmp.json', 'w') as f:
#     json.dump(t, f)
from ..config import *

def run(card) -> None:
  link = card['link']
  driver = webdriver.Chrome(service=service, options=options)
  driver.set_page_load_timeout(30)
  driver.get(link)
  WebDriverWait(driver, 10).until(
    lambda d: d.execute_script("return document.readyState") == "complete"
  )
  driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]').click()
  sleep(1)
  driver.find_element(By.XPATH, '//*[@id="form_text_1"]').send_keys(card['values']['firstname'] + ' ' + card['values']['lastname'])
  driver.find_element(By.XPATH, '//*[@id="form_text_2"]').send_keys(card['values']['email'])
  phone = card['values']['phone'][1:] if card['values']['phone'][0] == '8' else card['values']['phone'][2:]
  driver.find_element(By.XPATH, '//*[@id="form_text_3"]').send_keys(phone)
  driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(card['values']['cv'])
  driver.find_element(By.XPATH, '//*[@id="responseForm"]/div/form/div[11]/div/div/label').click()
  sleep(1)
  driver.find_element(By.CLASS_NAME, 'vacancy-response__send-btn').click()
  sleep(3)

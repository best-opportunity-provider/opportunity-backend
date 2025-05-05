from ..config import *

def run(card) -> None:
  link = card['link']
  driver.get(link)
  WebDriverWait(driver, 10).until(
    lambda d: d.execute_script("return document.readyState") == "complete"
  )
  driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]').click()
  sleep(1)
  driver.find_element(By.XPATH, '//*[@id="form_text_1"]').send_keys(card['values']['firstname'] + ' ' + card['values']['lastname'])
  driver.find_element(By.XPATH, '//*[@id="form_text_2"]').send_keys(card['values']['email'])
  driver.find_element(By.XPATH, '//*[@id="form_text_3"]').send_keys(card['values']['phone'])
  driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(card['values']['cv'])
  driver.find_element(By.XPATH, '//*[@id="responseForm"]/div/form/div[11]/div/div/label').click()
  sleep(1)
  driver.find_element(By.CLASS_NAME, 'vacancy-response__send-btn').click()
  sleep(3)

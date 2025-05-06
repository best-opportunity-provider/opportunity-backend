from ..config import *

def run(card) -> None:
  link = card['link']
  driver = webdriver.Chrome(service=service, options=options)
  driver.set_page_load_timeout(30)
  driver.get(link)
  sleep(2)

  driver.find_element(By.XPATH, '//*[@id=":Rbja6j6cvfesrnnjb:"]').click()
  sleep(1)

  driver.find_element(By.XPATH, '//*/input[@name="contactInfo.name"]').send_keys(card['values']['firstname'])
  driver.find_element(By.XPATH, '//*/input[@name="contactInfo.surname"]').send_keys(card['values']['lastname'])
  driver.find_element(By.XPATH, '//*/input[@name="contactInfo.phoneNumber"]').send_keys(card['values']['phone'])
  driver.find_element(By.XPATH, '//*/input[@name="contactInfo.dateOfBirth"]').send_keys(card['values']['birthday'])
  
  sleep(1)
  
  driver.find_element(By.XPATH, '//*[@id=":r5:"]').click()
  sleep(5)

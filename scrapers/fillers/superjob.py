from ..config import *
from datetime import datetime

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
  phone = card['values']['phone'][1:] if card['values']['phone'][0] == '8' else card['values']['phone'][2:]
  driver.find_element(By.XPATH, '//*/input[@name="contactInfo.phoneNumber"]').send_keys(phone)
  date_of_birth = datetime.fromisoformat(card['values']['birthday'])
  driver.find_element(By.XPATH, '//*/input[@name="contactInfo.dateOfBirth"]').send_keys(date_of_birth.strftime("%d.%m.%Y"))
  
  sleep(1)
  
  driver.find_element(By.XPATH, '//*[@id=":r5:"]').click()
  sleep(5)

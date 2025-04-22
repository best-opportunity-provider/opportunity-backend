from config import *

def fill_google_form(card) -> None:
  link = card['link']
  driver.get(link)

  driver.find_element(by="xpath", value="/html/body/div/div[3]/div/div[1]/div/div/div/div/div/div/div[1]/button").click()

  driver.find_element(by="xpath", value="/html/body/div[2]/div[3]/div/div[1]/div[2]/form/div[2]/div[1]/div[1]/div/div/div/input").send_keys(card['form']['name']['label'])
  driver.find_element(by="xpath", value="/html/body/div[2]/div[3]/div/div[1]/div[2]/form/div[2]/div[1]/div[2]/div/div/div/input").send_keys(card['form']['surename']['label'])
  driver.find_element(by="xpath", value="/html/body/div[2]/div[3]/div/div[1]/div[2]/form/div[2]/div[2]/div[1]/div/div/div/input").send_keys(card['form']['phone']['label'])
  driver.find_element(by="xpath", value="/html/body/div[2]/div[3]/div/div[1]/div[2]/form/div[2]/div[2]/div[2]/div/div/div/input").send_keys(card['form']['birthday']['label'])
  
  sleep(10)
  
  driver.find_element(by="xpath", value="/html/body/div[2]/div[3]/div/div[2]/div/button").click()

  sleep(10)
  
  driver.close()

tr = {
  "link": "https://changellenge.com/vacancy/inzhenyer-po-ekspluatacii-bazovykh-stanciy-t2-moskva/",
  "form": {
    "name": {
      "type": "string",
      "required": True,
      "label": "Введите ваше имя"
    },
    "email": {
      "type": "email",
      "required": True,
      "label": "Введите ваш адрес электронной почты"
    },
    "resume": {
      "type": "file",
      "required": True,
      "label": "Приложите обновленное резюме или CV (PDF предпочтительно)"
    },
    "transcript": {
      "type": "file",
      "required": True,
      "label": "Приложите текущий неофициальный или официальный транскрипт на английском языке (PDF предпочтительно)"
    }
  }
  }

fill_google_form(tr)
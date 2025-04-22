from config import *

def fill_habr_form(card) -> None:
  driver.get('https://account.habr.com/ru/ident/0TAKCUZlHJrEoNSIsrUrW-EtfkxmzOeZM4CeBnh5w5_n9tLP_TR0Gpn3ciqqA2HmMax_w8S6LEsAtzhat_jfGSHTsl8QD5sM6d1vzPQvaPEmKtwDaG4Li6VlJferyX1-RAmMPl7JgZ3RBQ1X7c35c21KCWqjLr_ZAip2T_Wg_qYn4z_jjD-BYtR1jZFYO2Bx9W2rSvS7wk-GAS6z')
  sleep(60)

  link = card['link']
  driver.get(link)

  driver.find_element(by="xpath", value="/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/form/div[1]/div/div[1]/div[2]/div/span[1]/span/input").send_keys(card['form']['desired_salary']['label'])
  driver.find_element(by="xpath", value="/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/form/div[1]/div/div[2]/div[2]/span[2]/div/textarea").send_keys(card['form']['cover_letter']['label'])
  
  sleep(10)
  
  driver.find_element(by="xpath", value="/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/form/div[2]/div/button").click()
  
  driver.close()

tr = {
  "link": "https://career.habr.com/vacancies/1000152860",
    "form": {
    "name": {
      "type": "string",
      "required": True,
      "label": "имя"
    },
    "email": {
      "type": "email",
      "required": True,
      "name": "dvjcbnsdfrb@gmail.com"
    },
    "desired_salary": {
      "type": "string",
      "required": True,
      "label": "88005553535"
    },
    "resume": {
      "type": "file",
      "required": True,
      "label": "Приложите ваше резюме"
    },
    "cover_letter": {
      "type": "textarea",
      "required": False,
      "label": "Сообщение нет"
    }
  }
  }

fill_habr_form(tr)
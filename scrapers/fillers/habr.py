from config import *

def fill_habr_form(card) -> None:
  try:
      driver.get('https://account.habr.com')
      wait = WebDriverWait(driver, 10)
      email = wait.until(EC.element_to_be_clickable((By.NAME, "email")))
      email.send_keys('gauterderfork@gmail.com')
      password = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
      password.send_keys('6zL-LGT-nEy-Pit')
      while driver.current_url != 'https://career.habr.com/vacancies?type=all': True
  except Exception as e:
      print(f"An error occurred: {e}")

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
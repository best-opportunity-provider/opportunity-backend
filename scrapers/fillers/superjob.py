from config import *

def run(card) -> None:
  link = card['link']
  driver.get(link)
  sleep(2)

  driver.find_element(by="xpath", value='//*[@id=":r1:"]').click()
  sleep(2)

  driver.find_element(by="xpath", value='//*/input[@name="contactInfo.name"]').send_keys(card['form']['name']['value'])
  driver.find_element(by="xpath", value='//*/input[@name="contactInfo.surname"]').send_keys(card['form']['surename']['value'])
  driver.find_element(by="xpath", value='//*/input[@name="contactInfo.phoneNumber"]').send_keys(card['form']['phone']['value'])
  driver.find_element(by="xpath", value='//*/input[@name="contactInfo.dateOfBirth"]').send_keys(card['form']['birthday']['value'])
  
  sleep(10)
  
  driver.find_element(by="xpath", value='//*[@id=":rj:"]').click()

  sleep(10)
  
  driver.close()

tr = {
    "link": "https://students.superjob.ru/stazhirovki/44386520/",
    "form":{
      "name": {
        "type": "string",
        'value': "Art"
      },
      "surename": {
        "type": "string",
        'value': "Zap"
      },
      "birthday": {
        "type": "string",
        'value': "12.12.2000"
      },
      "email": {
        "type": "email",
        'value': "12345678@mail.ru"
      },
      "phone": {
        "type": "string",
        'value': "8005553535"
      },
      "resume": {
        "type": "string",
        'value': "тшорарикудшгрмпиорлыукрошдпружолмриошжвалыярпшомрцукнгшрщапр икушорритыпш доыуекшщгнр пагнолуыкр шгдщапукрфшгд"
      }
    }
  }

run(tr)
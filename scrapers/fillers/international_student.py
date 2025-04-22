from config import *

def fill_inter_student_form(card) -> None:
  link = card['link']
  driver.get(link)
  
  values = []
  for val in card["form"].values():
    values.append(val['label'])

  pos = 0
  for it in range(1, 4):
    for jt in range(1, 7):
      if it == 3 and jt == 6:
        if BeautifulSoup(driver.page_source, "html.parser").find('div', class_='card card-body bg-light shadow rounded-0').find('img') is not None:
          response = requests.get('	https://www.internationalstudent.com' + BeautifulSoup(driver.page_source, "html.parser").find('div', class_='card card-body bg-light shadow rounded-0').find('img').get('src'))
          image = Image.open(BytesIO(response.content))
          txt = pytesseract.image_to_string(image, lang='eng').replace("\n", "")
          driver.find_element(by="xpath", value=f"/html/body/div[3]/div/div[1]/div/form/div[1]/div[{it}]/div[{jt}]/div/input").send_keys(txt)
      driver.find_element(by="xpath", value=f"/html/body/div[3]/div/div[1]/div/form/div[1]/div[{it}]/div[{jt}]/div/input").send_keys(123)
      pos += 1
      if pos == len(values):
        break
    if pos == len(values):
      break

  sleep(10)
  
  driver.find_element(by="xpath", value="/html/body/div[2]/div[3]/div/div[2]/div/button").click()

  sleep(10)
  
  driver.close()

tr = {
    "link": "https://www.internationalstudent.com/school-search/2661/usa/california/academy-of-chinese-culture-and-health-sciences/",
    "form": {
      "name": {
        "type": "string",
        "required": True,
        "label": "Art"
      },
      "email": {
        "type": "email",
        "required": True,
        "label": "12345678@gmail.com"
      },
      "phone": {
        "type": "tel",
        "required": True,
        "label": "8005553535"
      },
      "country": {
        "type": "string",
        "required": True,
        "label": "USA"
      },
      "city": {
        "type": "string",
        "required": True,
        "label": "New York"
      },
      "zip": {
        "type": "string",
        "required": True,
        "label": "10208"
      },
      "program": {
        "type": "string",
        "required": True,
        "label": "IT"
      },
      "start_date": {
        "type": "string",
        "required": True,
        "label": "12.12.2024"
      },
      "highest_degree": {
        "type": "string",
        "required": True,
        "label": "Highest Degree "
      },
      "degree_sought": {
        "type": "string",
        "required": True,
        "label": "Degree Sought"
      },
      "study_field": {
        "type": "string",
        "required": True,
        "label": "Intended Study Field"
      },
      "financial_qualifier": {
        "type": "string",
        "required": True,
        "label": "How will you pay for your education?"
      },
      "verify_code": {
        "type": "string",
        "required": True,
        "label": "Verify Code"
      },
      "usage_agreement": {
        "type": "boolean",
        "required": True,
        "label": "Usage Agreement"
      }
    }
  }

fill_inter_student_form(tr)
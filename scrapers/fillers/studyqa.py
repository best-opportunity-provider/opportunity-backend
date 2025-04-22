from config import *

def run(card) -> None:
    """
    Automates the process of filling out a Yandex form using Selenium WebDriver.

    Args:
        card (dict): A dictionary containing the form data and its structure.
            Expected keys:
                - 'link' (str): URL of the Yandex opportunity.
                - 'form' (dict): Form fields with their values.
                    - 'name' : 'value'
                    - 'cv' : 'value'
                    ...

    Steps:
        1. Navigate to the Yandex opportunity's URL provided in `card['link']`.
        2. Fill in the form fields based on the structure of `card['form']`.
        3. Mark specific checkboxes.
        4. Close the browser after submission.

    Note:
       We take it for granted that the fields in the dictionary card['form'] 
      are in the same order as the fields in the Yandex form.
    """
    link = card['link'] + '#'
    driver.get(link)
    sleep(2)

    # Fill in standard input fields.
    driver.find_element(by="xpath", value='//*[@id="internship_lead_form"]/div[2]/div/div[1]/div/input').send_keys(card['form']['name']['value'])
    sleep(1)
    driver.find_element(by="xpath", value='//*[@id="internship_lead_form"]/div[2]/div/div[2]/div/input').send_keys(card['form']['surename']['value'])
    sleep(1)
    driver.find_element(by="xpath", value='//*[@id="internship_lead_form"]/div[2]/div/div[3]/div/input').send_keys(card['form']['email']['value'])
    sleep(1)
    driver.find_element(by="xpath", value='//*[@id="internship_lead_form"]/div[2]/div/div[4]/div/input').send_keys(card['form']['phone']['value'])
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="internship_lead_form"]/div[2]/div/div[5]/div').click()
    sleep(1)
    driver.find_element(By.XPATH, '/html/body/span/span/span[1]/input').send_keys(card['form']['contry']['value'])
    sleep(1)
    pyautogui.press("Enter")
    sleep(1)
    driver.find_element(by="xpath", value='//*[@id="internship_lead_form"]/div[2]/div/div[6]/div/input').send_keys(card['form']['city']['value'])
    sleep(1)
    driver.find_element(by="xpath", value='//*[@id="internship_lead_form"]/div[2]/div/div[7]/div/input').send_keys(card['form']['age']['value'])
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="internship_lead_form"]/div[2]/div/div[8]/div/div').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="select2-internship_lead_gender-im-results"]/li[' + ('1' if card['form']['sex']['value'] == 'женский' else '2') + ']').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="select2-internship_lead_lang_level-dz-container"]').click()
    sleep(1)
    lang_levels = ['Beginner', 'Intermediate', 'Upper-Intermediate', 'Advanced', 'Proficiency']
    driver.find_element(By.XPATH, '//*[@id="select2-internship_lead_lang_level-k9-results"]/li[' + str(lang_levels.index(card['form']['language_level']['value']) + 1) + ']').click()
    sleep(1)
    driver.find_element(by="xpath", value='//*[@id="internship_submit_btn"]').click()
    sleep(1)

tr = {
    'link': 'https://ru.studyqa.com/internships/view/aples-hotel-internship',
    'form': {
      "name": {
        "type": "string",
        "value": "Art"
      },
      "surename": {
        "type": "string",
        "value": "Zap"
      },
      "age": {
        "type": "string",
        "value": "24"
      },
      "sex": {
        "type": "string",
        "value": "мужской"
      },
      "email": {
        "type": "email",
        "value": "12345678@mail.ru"
      },
      "phone": {
        "type": "string",
        "value": "+78005553535"
      },
      "city": {
        "type": "string",
        "value": "Albania"
      },
      "contry": {
        "type": "string",
        "value": "Albania"
      },
      "language_level": {
        "type": "string",
        "value": "Intermediate"
      },
      "cv": {
        "type": "file",
        "value": "C:\VSC\BestOpportunityProvider\cv.pdf",
      },
      "cover_letter": {
        "type": "textarea",
        "value": "Прикрепите сопроводительное письмо (необязательно)"
      }
    }
}

run(tr)
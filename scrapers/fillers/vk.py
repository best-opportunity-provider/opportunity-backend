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
    link = card['link']
    driver.get(link)
    sleep(2)

    # Fill in standard input fields.
    driver.find_element(by="xpath", value='//*/input[@name="first_name"]').send_keys(card['form']['name']['value'])
    sleep(1)
    driver.find_element(by="xpath", value='//*/input[@name="last_name"]').send_keys(card['form']['surename']['value'])
    sleep(1)
    driver.find_element(by="xpath", value='//*/input[@name="date_of_birth"]').send_keys(card['form']['birthday']['value'])
    sleep(1)
    driver.find_element(By.XPATH, '//*/div[@name="sex"]//div[@class="ant-select-selector"]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*/div[contains(@class, "ant-select-item-option") and @title="' + card['form']['sex']['value'] + '"]').click()
    sleep(1)
    driver.find_element(by="xpath", value='//*/input[@name="email"]').send_keys(card['form']['email']['value'])
    sleep(1)
    driver.find_element(by="xpath", value='//*/input[@name="phone_number"]').send_keys(card['form']['phone']['value'])
    sleep(1)
    driver.find_element(by="xpath", value='//*[@id="rc_select_1"]').send_keys(card['form']['city']['value'])
    sleep(1)
    pyautogui.press("Enter")
    sleep(1)
    driver.find_element(by="xpath", value='//*[@id="rc_select_2"]').send_keys(card['form']['university']['value'])
    sleep(1)
    pyautogui.press("Enter")
    sleep(1)
    driver.find_element(by="xpath", value='//*[@id="rc_select_3"]').send_keys(card['form']['faculty']['value'])
    sleep(1)
    pyautogui.press("Enter")
    sleep(1)
    driver.find_element(By.XPATH, '//*/div[@name="education_stage"]//div[@class="ant-select-selector"]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*/div[contains(@class, "ant-select-item-option") and @title="' + card['form']['education_stage']['value'] + '"]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*/div[@name="course"]//div[@class="ant-select-selector"]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*/div[contains(@class, "ant-select-item-option") and @title="' + card['form']['course']['value'] + '"]').click()
    sleep(1)
    driver.find_element(by="xpath", value='//*/input[@name="year_admission"]').send_keys(card['form']['year_admission']['value'])
    sleep(1)
    driver.find_element(by="xpath", value='//*/input[@name="year_graduation"]').send_keys(card['form']['year_graduation']['value'])
    sleep(1)
    dropdown_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[@name="language_level"]//div[contains(@class, "ant-select-selector")]')
        )
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", dropdown_element)

    ActionChains(driver).move_to_element(dropdown_element).pause(0.5).click().perform()
    sleep(1)
    driver.find_element(By.XPATH, '//*/div[contains(@class, "ant-select-item-option") and @title="' + card['form']['language_level']['value'] + '"]').click()
    sleep(1)
        
    driver.find_element(by="xpath", value='//*/input[@type="file"]').send_keys(card['form']['cv']['value'])
    sleep(1)
    driver.find_element(by="xpath", value='//*[@id="basic"]/div[5]/div[2]/div/textarea').send_keys(card['form']['cover_letter']['value'])
    sleep(1)
    driver.find_element(by="xpath", value='//*[@id="basic"]/div[6]/div[1]/label/span[1]/input').click()
    sleep(1)
    driver.find_element(by="xpath", value='//*[@id="basic"]/div[6]/div[2]/button').click()
    sleep(1)

tr = {
    'link': 'https://internship.vk.company/vacancy/1092',
    'form': {
      "name": {
        "type": "string",
        "value": "Art"
      },
      "surename": {
        "type": "string",
        "value": "Zap"
      },
      "birthday": {
        "type": "string",
        "value": "12.12.2000"
      },
      "sex": {
        "type": "string",
        "value": "женский"
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
        "value": "Казань"
      },
      "university": {
        "type": "string",
        "value": "МГТУ имени Н. Э. Баумана"
      },
      "faculty": {
        "type": "string",
        "value": "Аэрокосмический факультет"
      },
      "education_stage": {
        "type": "string",
        "value": "Специалитет"
      },
      "course": {
        "type": "string",
        "value": "3 курс"
      },
      "year_admission": {
        "type": "string",
        "value": "2024"
      },
      "year_graduation": {
        "type": "string",
        "value": "2028"
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
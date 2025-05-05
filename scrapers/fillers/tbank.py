from config import *

def run(card) -> bool:
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
    elems = driver.find_elements(By.CLASS_NAME, 'cbe3NUl8b abSXczQlQ')
    if len(elems) == 2:
      elems[0].send_keys(card['form']['surename']['value'] + ' ' + card['form']['name']['value'] + ' ' + card['form']['patronymic']['value'])
      elems[1].send_keys(card['form']['email']['value'])
    sleep(2)
    button = driver.find_elements(By.CLASS_NAME, 'abVWg4qmF hbVWg4qmF')
    if len(button) == 1:
      button[0].click()
    return True

tr = {
    'link': 'https://tochka.com/hr/it/technical-product-manager/',
    'form': {
      "name": {
        "type": "string",
        "value": "Art"
      },
      "surename": {
        "type": "string",
        "value": "Zap"
      },
      "patronymic": {
        "type": "string",
        "value": "Sur"
      },
      "telegram": {
        "type": "string",
        "value": "@noil"
      },
      "email": {
        "type": "email",
        "value": "12345678@mail.ru"
      },
      "phone": {
        "type": "string",
        "value": "+78005553535"
      },
      "cv": {
        "type": "file",
        "value": "C:\\Users\\zarch\\Downloads\\png2pdf.pdf"
      },
      "cover_letter": {
        "type": "textarea",
        "value": "Прикрепите сопроводительное письмо (необязательно)"
      }
    }
}

run(tr)
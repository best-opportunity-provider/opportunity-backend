from config import *

def fill_yandex_forms(card) -> None:
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

    # Fill the 'resume' field.
    driver.find_element(by="name", value="answer_resume_type_file").send_keys(card['form']['cv']['value'])

    # Gather all values except 'link' and 'resume'.
    values = []
    for attribute in card['form']:
        if attribute != 'link' and attribute != 'cv':
            values.append(card['form'][attribute]['value'])

    pos = 0

    # Parse the page source to locate input fields.
    dom = etree.HTML(driver.page_source)
    tree = etree.ElementTree(dom)

    # Fill in standard input fields.
    form_inputs = dom.xpath('//*/span/span/input')
    for thing in form_inputs:
        driver.find_element(by="xpath", value=tree.getpath(thing)).send_keys(values[pos])
        pos += 1

    # Fill in text areas.
    form_inputs = dom.xpath('//*/textarea')
    for thing in form_inputs:
        driver.find_element(by="xpath", value=tree.getpath(thing)).send_keys(values[pos])
        pos += 1

    # Select checkboxes.
    driver.find_element(by="xpath", value="/html/body/div[1]/div/main/form/div/div[10]/div/div/div[1]/label/span[1]/input").click()
    driver.find_element(by="xpath", value="/html/body/div[1]/div/main/form/div/div[11]/div/div/div[1]/label/span[1]/input").click()
    driver.find_element(by="xpath", value="/html/body/div[1]/div/main/form/div/div[12]/div/div/div[1]/label/span[1]/input").click()

    # Close the browser.
    driver.close()

tr = {
  "link": "https://yandex.ru/jobs/vacancies/menedzherstazher-po-svyazyam-s-obschestvennostyu-27231",
  "form_link": "https://forms.yandex.ru/surveys/10029744.445a248a3887ab9ca79052d4b31d1a42cf1ad25c?publication_id=27231",
  
  "name": "Менеджер-стажер по связям с общественностью",
  "short_description": "Стажировка в команде бизнес-группы Поиска и рекламных технологий.",
  "description": "Команда бизнес-группы Поиска и рекламных технологий ищет стажёра, который усилит команду внешних коммуникаций. Вы будете помогать в решении задач блока, поддерживать ключевой продукт.",
  
  "provider": "Яндекс",
  "logo": "https://yastatic.net/q/logoaas/v2/Яндекс.svg?single=1&viewBox=1",
  
  "requirements": [
    "Хотите работать в B2B-коммуникациях.",
    "Умеете просто и увлекательно рассказывать о сложном.",
    "Готовы работать на результат и измерять его.",
    "Готовы самостоятельно вести проекты и составлять бюджеты.",
    "Умеете или хотите научиться работать с журналистами и лидерами мнений.",
    "Имеете отличные коммуникативные навыки и с лёгкостью находите общий язык с разными людьми."
  ],
  "advantages": [
    "Оплачиваемую стажировку сроком 3 месяца.",
    "Полный рабочий день (40 часов в неделю).",
    "Офисный формат работы.",
    "Сильную команду, у которой можно многому научиться.",
    "Компенсацию затрат на питание."
  ],
  "target": [
    "Студенты и выпускники, интересующиеся карьерой в сфере коммуникаций."
  ],
  "discipline": [
    "Маркетинг и коммуникации"
  ],
  
  "place": [
    "Москва"
  ],
  "period_of_internship": "3 месяца",
  
  "selection_stages": [
    {
      "name": "Отбор резюме",
      "period": "1 неделя",
      "objectives": [
        "Проверка соответствия кандидата требованиям вакансии.",
        "Выбор наиболее подходящих кандидатов для дальнейшего этапа."
      ]
    },
    {
      "name": "Собеседование",
      "period": "1 неделя",
      "objectives": [
        "Личное знакомство с кандидатами.",
        "Оценка коммуникативных навыков и опыт работы."
      ]
    },
    {
      "name": "Тестовое задание",
      "period": "3 дня",
      "objectives": [
        "Проверка практических навыков кандидата.",
        "Оценка способности работать под давлением."
      ]
    }
  ],
  
  "allowance": "Оплачиваемая стажировка",
  "expenses": "Компенсация затрат на питание",
  
  "additional": [
    {
      "title": "Возможность роста",
      "description": "После успешного прохождения стажировки возможен переход на постоянную работу в компании."
    },
    {
      "title": "Обучение",
      "description": "Проведение мастер-классов и тренингов для развития навыков."
    },
    {
      "title": "Командные мероприятия",
      "description": "Участие в командных мероприятиях и корпоративных праздниках."
    }
  ],
  
  "tags": [
    "Стажировка",
    "Коммуникации",
    "Маркетинг",
    "Яндекс"
  ],
  
  "form": {
    "name": {
        "type": "string",
        "label": "Art"
      },
      "surename": {
        "type": "string",
        "label": "Zap"
      },
      "birthday": {
        "type": "string",
        "label": "12.12.2000"
      },
      "email": {
        "type": "email",
        "label": "12345678@mail.ru"
      },
      "phone": {
        "type": "string",
        "label": "+78005553535"
      },
      "resume": {
        "type": "string",
        "label": "тшорарикудшгрмпиорлыукрошдпружолмриошжвалыярпшомрцукнгшрщапр икушорритыпш доыуекшщгнр пагнолуыкр шгдщапукрфшгд"
      },
    "cover_letter": {
      "type": "textarea",
      "label": "Прикрепите сопроводительное письмо (необязательно)"
    }
  }
}
fill_yandex_forms(tr)
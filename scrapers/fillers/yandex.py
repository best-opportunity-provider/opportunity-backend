from ..config import *

def run(card) -> None:
    """
    Automates the process of filling out a Yandex form using Selenium WebDriver.

    Args:
        card (dict): A dictionary containing the form data and its structure.
            Expected keys:
                - 'form_link' (str): URL of the Yandex opportunity.
                - 'form' (dict): Form fields with their values.
                    - 'name' : 'value'
                    - 'cv' : 'value'
                    ...

    Steps:
        1. Navigate to the Yandex opportunity's URL provided in `card['form_link']`.
        2. Fill in the form fields based on the structure of `card['form']`.
        3. Mark specific checkboxes.
        4. Close the browser after submission.

    Note:
       We take it for granted that the fields in the dictionary card['form'] 
      are in the same order as the fields in the Yandex form.
    """
    link = card['link']
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_page_load_timeout(30)
    driver.get(link)
    wait = WebDriverWait(driver, 20)
    sleep(2)

    driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(card['values']['cv'])
    sleep(0.5)
    driver.find_element(By.ID, 'answer_param_name').send_keys(card['values']['firstname'])
    sleep(0.5)
    driver.find_element(By.ID, 'answer_param_surname').send_keys(card['values']['lastname'])
    sleep(0.5)
    driver.find_element(By.ID, 'answer_param_phone').send_keys(card['values']['phone'])
    sleep(0.5)
    driver.find_element(By.ID, 'answer_non_profile_email_5257').send_keys(card['values']['email'])

    # # Gather all values except 'link' and 'resume'.
    # values = []
    # for attribute in card:
    #     if attribute != 'link' and attribute != 'cv':
    #         values.append(card[attribute])

    # pos = 0

    # # Parse the page source to locate input fields.
    # dom = etree.HTML(driver.page_source)
    # tree = etree.ElementTree(dom)

    # # Fill in standard input fields.
    # form_inputs = dom.xpath('//*/span/span/input')
    # for thing in form_inputs:
    #     driver.find_element(by="xpath", value=tree.getpath(thing)).send_keys(values[pos])
    #     pos += 1

    # Fill in text areas.
    # form_inputs = dom.xpath('//*/textarea')
    # for thing in form_inputs:
    #     driver.find_element(by="xpath", value=tree.getpath(thing)).send_keys(values[pos])
    #     pos += 1

    # Select checkboxes.
    checkboxes = wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, "//input[@type='checkbox']")
    ))
    
    for checkbox in checkboxes:
        driver.execute_script("arguments[0].click();", checkbox)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)
    
    # Submit form
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit']")
    ))
    submit_button.click()
    sleep(5)


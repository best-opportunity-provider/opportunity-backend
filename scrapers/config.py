import requests
import itertools
from bs4 import BeautifulSoup
from lxml import etree 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
import urllib, json
from io import BytesIO
import time
from time import sleep

import pytesseract
from PIL import Image
from typing import TypedDict

# Configure Selenium WebDriver using ChromeDriver.
service = ChromeService(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--no-sandbox")  # Обход ограничений безопасности ОС
options.add_argument("--disable-dev-shm-usage")  # Решение проблем с нехваткой памяти
# options.add_argument("--headless")  # Option for headless mode.
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

class CategorizedOpportunityDump(TypedDict):
    url: str
    main_html: str
    form_html: str | None

from urllib.parse import urlparse
import threading
from typing import Callable
from concurrent.futures import ThreadPoolExecutor 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from .config import *
from .parsers import GETTER_LINKS, HANDLERS

def get_opportunity_links(
    filename: str = "links.txt",
    max_threads: int = 3 
) -> None:
    errors = []
    lock = threading.Lock()

    def run_getter(getter: Callable) -> None:
        try:
            driver = webdriver.Chrome(
                service=service, 
                options=options
            )
            driver.set_page_load_timeout(30)
            
            try:
                getter(driver, filename)
            except Exception as e:
                with lock:
                    errors.append(f"Failed in {getter.__name__}: {str(e)}")
            finally:
                driver.quit()
        except Exception as e:
            with lock:
                errors.append(f"Failed to init driver for {getter.__name__}: {str(e)}")

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(run_getter, getter) for getter in GETTER_LINKS]
        
        for future in futures:
            try:
                future.result()
            except Exception as e:
                pass

def html_opportunity(url: str) -> CategorizedOpportunityDump | None:
    handler = HANDLERS.get(urlparse(url).netloc)
    if handler is None:
        print(f'Couldn\'t find handler for URL: {url}')
        return None
    opportunity_dump = handler(url)
    return opportunity_dump


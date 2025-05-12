# from scrapers import parse_all
from scrapers.parsers.yandex import get_links
from scrapers.fillers.yandex import run
from scrapers.config import *
# from .run import start_pipeline

tr = {
    "link" : "https://forms.yandex.ru/surveys/10029744.445a248a3887ab9ca79052d4b31d1a42cf1ad25c?publication_id=33359&submission_jobs_id=1747051532132333591201569471684932767&publication_url=http%3A%2F%2Fyandex.ru%2Fjobs%2Fvacancies%2Fmenedzher-proektov-v-market-33359&_=%2F&iframe=1&theme=jobs&lang=ru",
    # "link" : "https://careers.croc.ru/vacancies/razrabotchik-distributiva-linux/",
    # "link" : "https://students.superjob.ru/stazhirovki/47102401/",
    "values": {
        "firstname": "Петр",
        "lastname": "Андреев",
        "birthday": "2010-08-12",
        "sex":  0,
        "email": "gabat@gmail.com",
        "phone": "+79892345167",
        "cv": "C:\VSC\BestOpportunityProvider\cv.pdf"
    }
}

# driver1 = webdriver.Chrome(
#                 service=service, 
#                 options=options
#             )
# driver1.set_page_load_timeout(30)
# get_links(driver1, 'test.txt')
# driver1.close()
run(tr)
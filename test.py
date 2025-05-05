# from scrapers import parse_all
from scrapers.fillers.yandex import run
# from .run import start_pipeline

tr = {
    "link" : "https://forms.yandex.ru/surveys/10029744.445a248a3887ab9ca79052d4b31d1a42cf1ad25c/?publication_id=7112&submission_jobs_id=174646853776971121201569471684932767&publication_url=http%3A%2F%2Fyandex.ru%2Fjobs%2Fvacancies%2Frazrabotchik-platformi-dannih-v-yandex-cloud-7112&_=%2F&iframe=1&theme=jobs&lang=ru",
    "values": {
        "firstname": "Петр",
        "lastname": "Андреев",
        "birthday": "12.08.2010",
        "sex":  0,
        "email": "gabat@gmail.com",
        "phone": "+79892345167",
        "cv": "C:\VSC\BestOpportunityProvider\cv.pdf"
    }
}


run(tr)
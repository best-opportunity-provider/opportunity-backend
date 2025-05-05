# from scrapers import parse_all
from scrapers.fillers.croc import run
# from .run import start_pipeline

tr = {
    "link" : "https://careers.croc.ru/vacancies/setevoy-inzhener1/",
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
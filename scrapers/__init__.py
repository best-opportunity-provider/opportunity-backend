from urllib.parse import urlparse
from .config import *

from .parsers import *

# GETTER_LINKS = [
#     get_links_changellenge,
#     get_links_croc,
#     get_links_futuretoday,
#     get_links_goabroad,
#     get_links_google,
#     get_links_habr,
#     get_links_international_student,
#     get_links_jobby,
#     get_links_linkedin,
#     get_links_studyqa,
#     get_links_superjob,
#     get_links_tbank,
#     get_links_tochka,
#     get_links_vk,
#     get_links_yandex,
# ]

HANDLERS = {
    'changellenge.com': run_changellenge,
    'www.changellenge.com': run_changellenge,
    'careers.croc.ru': run_croc,
    'it.fut.ru': run_futuretoday,
    'fut.ru': run_futuretoday,
    'www.goabroad.com': run_goabroad,
    'www.google.com': run_google,
    'career.habr.com': run_habr,
    'www.internationalstudent.com': run_international_student,
    'my.jobby.ai': run_jobby,
    'www.linkedin.com': run_linkedin,
    'ru.studyqa.com': run_studyqa,
    'students.superjob.ru': run_superjob,
    'education.tbank.ru': run_tbank,
    'tochka.com': run_tochka,
    'internship.vk.company': run_vk,
    'yandex.ru': run_yandex,
}


# def get_opportunity_links() -> list[str]:
#     links = []
#     for getter in GETTER_LINKS:
#         links += getter()
#     return links
    

def parse_opportunity(url: str) -> CategorizedOpportunityDump:
    handler = HANDLERS.get(urlparse(url).netloc)
    if handler is None:
        raise ValueError(f'Couldn\'t find handler for URL: {url}')
    opportunity_dump = handler(url)
    return opportunity_dump


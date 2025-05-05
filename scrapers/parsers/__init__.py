from .changellenge import run as run_changellenge
from .croc import run as run_croc
from .futuretoday import run as run_futuretoday
from .goabroad import run as run_goabroad
from .google import run as run_google
from .habr import run as run_habr
from .international_student import run as run_international_student
from .jobby import run as run_jobby
from .linkedin import run as run_linkedin
from .studyqa import run as run_studyqa
from .superjob import run as run_superjob
from .tbank import run as run_tbank
from .tochka import run as run_tochka
from .vk import run as run_vk
from .yandex import run as run_yandex
from .changellenge import get_links as get_links_changellenge
from .croc import get_links as get_links_croc
from .futuretoday import get_links as get_links_futuretoday
from .goabroad import get_links as get_links_goabroad
from .google import get_links as get_links_google
from .habr import get_links as get_links_habr
from .international_student import get_links as get_links_international_student
from .jobby import get_links as get_links_jobby
from .linkedin import get_links as get_links_linkedin
from .studyqa import get_links as get_links_studyqa
from .superjob import get_links as get_links_superjob
from .tbank import get_links as get_links_tbank
from .tochka import get_links as get_links_tochka
from .vk import get_links as get_links_vk
from .yandex import get_links as get_links_yandex

GETTER_LINKS = [
    # get_links_changellenge,
    get_links_croc,
    # get_links_futuretoday,
    # get_links_goabroad,
    # get_links_google,
    # get_links_habr,
    # get_links_international_student,
    # get_links_jobby,
    # get_links_linkedin,
    # get_links_studyqa,
    get_links_superjob,
    # get_links_tbank,
    # get_links_tochka,
    # get_links_vk,
    get_links_yandex,
]

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

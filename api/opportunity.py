from .config import *

def update_opportunity(lang: str, id: int, body: dict) -> requests.Request:
    response = requests.patch(
        f'{API_HOST}:{API_PORT}/{lang}/private/opportunity/?id={id}', json=body
    )
    return response


def create_opportunity(body: dict) -> requests.Request:
    response = requests.post(
        f'{API_HOST}:{API_PORT}/private/opportunity', json=body
    )
    return response

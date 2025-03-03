# ===== Logging config =====

import logging
import os
from datetime import datetime

LOGS_FOLDER = f'logs/{datetime.now().strftime("%Y.%m.%d")}'
LOG_NAME = datetime.now().strftime('%H-%M-%S')

os.makedirs(LOGS_FOLDER, exist_ok=True)
logging.basicConfig(
    filename=f'{LOGS_FOLDER}/{LOG_NAME}.log',
    format='[%(levelname)s @ %(asctime)s] %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG,
)

logger = logging.getLogger()

# ===== App config =====

HOST: str = '127.0.0.1'
PORT: int = 8004

from fastapi import FastAPI

app = FastAPI()

import logging

from imdb_scraper import PROJECT_PATH

LOG_DIR = PROJECT_PATH / 'logs'
LOG_DIR.mkdir(exist_ok=True)

logger = logging.getLogger('app')
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(LOG_DIR / 'app.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

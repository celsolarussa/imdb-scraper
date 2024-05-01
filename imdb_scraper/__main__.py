import requests

from imdb_scraper import PROJECT_PATH
from imdb_scraper.config import logger
from imdb_scraper.scraper import imdb_scraper, utils


def get_page_text(url: str) -> str:
    """
    Makes a GET request to the provided URL and returns the response text.

    Args:
        url (str): The URL to make the request to.

    Returns:
        str: The response text.
    """
    headers = {
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    }
    try:
        response = requests.get(url, headers=headers)
        logger.info(f'Status code: {response.status_code}')
        return response.text
    except requests.exceptions.RequestException as e:
        logger.error(f'Error: {e}')


def main():
    """
    Main function that scrapes data from IMDB and saves the results in a JSON file.
    """
    logger.info('Starting the scraping process.')
    url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
    processed_dir = PROJECT_PATH / 'processed'
    processed_dir.mkdir(exist_ok=True)

    page_text = get_page_text(url)
    logger.info('Page text retrieved successfully.')
    data = imdb_scraper.scrape(page_text)
    logger.info('Data scraped successfully.')
    utils.save_data_in_json_file(processed_dir, data)
    logger.info('Data saved in JSON file.')


if __name__ == '__main__':
    main()

from typing import List

from bs4 import BeautifulSoup
from bs4.element import Tag
from tqdm import tqdm

from imdb_scraper.config import logger
from imdb_scraper.scraper.entities import AgeRating, MovieCardModel


def convert_votes_to_integer(vote_count: str) -> int:
    """
    Converts a vote count from string to int.

    Args:
        vote_count (str): The vote count as a string. It may contain 'M' for millions or 'K' for thousands.

    Returns:
        int: The vote count as an integer.
    """

    aux = vote_count.replace('(', '').replace(')', '').replace('M', '').replace('K', '')

    if 'M' in vote_count:
        return int(float(aux) * 1_000_000)
    elif 'K' in vote_count:
        return int(float(aux) * 1_000)
    else:
        raise ValueError('Invalid vote count format')


def convert_duration_time_to_integer(duration_time: str) -> int:
    """
    Converts a duration time from string to int.

    Args:
        duration_time (str): The duration time as a string. It may contain 'h' for hours and 'm' for minutes.

    Returns:
        int: The duration time in minutes.
    """

    if 'h' not in duration_time:
        return int(duration_time.replace('m', ''))
    elif 'm' not in duration_time:
        return int(duration_time.replace('h', '')) * 60

    hours, minutes = duration_time.split('h')

    return int(hours) * 60 + int(minutes.replace('m', ''))


def convert_age_rating_to_enum(age_rating: str) -> AgeRating:
    """
    Converts an age rating from string to enum.

    Args:
        age_rating (str): The age rating as a string.

    Returns:
        AgeRating: The age rating as an enum.
    """

    try:
        return AgeRating(age_rating.replace(' ', '').upper())
    except KeyError:
        return AgeRating.UNKNOWN


def _scrape(element: Tag) -> MovieCardModel:
    """
    Scrapes a tag element and returns a movie card model.

    Args:
        element (Tag): The tag element to be scraped.

    Returns:
        MovieCardModel: The scraped movie card model.
    """

    title_text = element.find('h3', class_='ipc-title__text').text
    rank_position, movie_title = title_text.split('. ', 1)
    poster_url = element.find('img', class_='ipc-image')['src']

    metadata_items = [
        aux.text for aux in element.find_all('span', class_='cli-title-metadata-item')
    ]

    if len(metadata_items) < 3:
        release_year, duration_time = metadata_items
        age_rating = 'NOTRATED'
    else:
        release_year, duration_time, age_rating = metadata_items

    imdb_rating, vote_count = (
        element.find('span', class_='ipc-rating-star').text.replace('\xa0', ' ').split(' ')
    )

    endpoint_more_info = element.find('a', class_='ipc-title-link-wrapper')['href']
    more_info_url = f'https://www.imdb.com{endpoint_more_info}'

    return MovieCardModel(
        rank_position=int(rank_position),
        title=movie_title,
        poster_url=poster_url,
        release_year=int(release_year),
        duration_time_in_minutes=convert_duration_time_to_integer(duration_time),
        age_rating=convert_age_rating_to_enum(age_rating),
        imdb_rating=float(imdb_rating),
        vote_count=convert_votes_to_integer(vote_count),
        more_info_url=more_info_url,
    )


def get_li_tags_from_page(page_text: str) -> List[Tag]:
    """
    Gets all li tags from a page text.

    Args:
        page_text (str): The text of the page to be parsed.

    Returns:
        List[Tag]: A list of li tags.
    """

    soup = BeautifulSoup(page_text, 'html.parser')
    ul = soup.find('ul', class_='ipc-metadata-list')

    return ul.find_all('li')


def scrape(page_text: str) -> List[MovieCardModel]:
    """
    Scrapes a page text and returns a list of movie card models.

    Args:
        page_text (str): The text of the page to be scraped.

    Returns:
        List[MovieCardModel]: A list of movie card models.
    """

    cards = get_li_tags_from_page(page_text)

    logger.info(f'Scraping {len(cards)} movie cards.')

    return [_scrape(card) for card in tqdm(cards)]

import json
from pathlib import Path
from typing import List

from imdb_scraper.scraper.entities import MovieCardModel


def save_data_in_json_file(processed_dir: Path, data: List[MovieCardModel]):
    """
    Saves the provided data in a JSON file in the processed directory.

    First, it converts the MovieCardModel objects into dictionaries and replaces the AgeRating objects with their string representations.
    Then, it writes the data to the data.json file in the processed directory.

    Args:
        processed_dir (Path): The directory where the JSON file should be saved.
        data (List[MovieCardModel]): The list of MovieCardModel objects to be saved.
    """

    data_as_dicts = [movie_card.__dict__ for movie_card in data]

    for movie_card in data_as_dicts:
        movie_card['age_rating'] = movie_card['age_rating'].name

    with open(processed_dir / "data.json", "w") as file:
        json.dump(data_as_dicts, file, indent=4)

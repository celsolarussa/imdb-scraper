from pathlib import Path
from unittest.mock import mock_open, patch

from imdb_scraper.scraper.entities import AgeRating, MovieCardModel
from imdb_scraper.scraper.utils import save_data_in_json_file


def test_save_data_in_json_file():
    movie_card = MovieCardModel(
        rank_position=1,
        title='The Shawshank Redemption',
        poster_url='https=//m.media-amazon.com/images/M/MV5BNDE3ODcxYzMtY2YzZC00NmNlLWJiNDMtZDViZWM2MzIxZDYwXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_QL75_UX140_CR0,1,140,207_.jpg',
        release_year=1994,
        duration_time_in_minutes=142,
        age_rating=AgeRating.R,
        imdb_rating=9.3,
        vote_count=2900000,
        more_info_url='https://www.imdb.com/title/tt0111161/?ref_=chttp_t_1',
    )
    data = [movie_card]
    processed_dir = Path('/test/path')

    with patch('builtins.open', mock_open()) as mock_file:
        save_data_in_json_file(processed_dir, data)

    mock_file.assert_called_once_with(processed_dir / "data.json", "w")

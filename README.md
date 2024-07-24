# IMDB Scraper

This is a simple web scraper that scrapes the IMDB website for the top 250 movies of all time. It uses the BeautifulSoup library to parse the HTML and extract the relevant information.

## Output Data

The scraper saves the scraped data in a JSON file (`processed/data.json`). Each movie is represented as a JSON object with the following structure:

```json
[
    {
        "rank_position": 1,
        "title": "The Shawshank Redemption",
        "poster_url": "https://m.media-amazon.com/images/M/MV5BNDE3ODcxYzMtY2YzZC00NmNlLWJiNDMtZDViZWM2MzIxZDYwXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_QL75_UX140_CR0,1,140,207_.jpg",
        "release_year": 1994,
        "duration_time_in_minutes": 142,
        "age_rating": "R",
        "imdb_rating": 9.3,
        "vote_count": 2900000,
        "more_info_url": "https://www.imdb.com/title/tt0111161/?ref_=chttp_t_1"
    },
]
```

## Installation

To install the required dependencies, run the following command:
```
pip install -r requirements.txt
```

## Usage

To run the scraper, execute the main script:
```
python -m imdb_scraper
```

This will start the scraping process. The scraper will log its progress to app.log and save the scraped data in `processed/data.json`.

## Testing

The project includes a suite of tests in the tests/ directory. These tests cover the scraping functions and utilities.

To run the tests, execute the following command:
```
pytest
```

## Features

- Scrapes data from the IMDB Top 250 movies list.
- Saves the scraped data in a JSON file.
- Logs the scraping process.

## Dependencies

The project uses the following Python libraries:

- BeautifulSoup for parsing HTML.
- pytest for testing.
- tqdm for progress bars.
- logging for logging.

## License

This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE) file for details.

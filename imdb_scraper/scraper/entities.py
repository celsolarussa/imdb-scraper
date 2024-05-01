from dataclasses import dataclass
from enum import Enum


class AgeRating(Enum):
    """
    An enum to represent the possible age ratings of a movie on IMDB.

    Attributes:
        G: All audiences admitted.
        PG: Parental guidance suggested. Some material may not be suitable for children.
        PG13: Parents strongly cautioned. Some material may be inappropriate for children under 13.
        R: Restricted. Under 17 requires accompanying parent or adult guardian.
        NC17: No one 17 and under admitted.
        NOTRATED: The movie has not been rated.
        APPROVED: The movie has been approved for screening.
        PASSED: The movie has been approved for screening.
        UNKNOWN: The age rating of the movie is unknown.
    """

    G = 'G'
    PG = 'PG'
    PG13 = 'PG-13'
    R = 'R'
    NC17 = 'NC-17'
    NOTRATED = 'NOTRATED'
    APPROVED = 'APPROVED'
    PASSED = 'PASSED'
    UNKNOWN = 'UNKNOWN'


@dataclass
class MovieCardModel:
    """
    A model to represent a movie card on IMDB.

    Attributes:
        rank_position (int): The movie's position in the IMDB ranking.
        title (str): The title of the movie.
        poster_url (str): The URL of the movie's poster.
        release_year (int): The release year of the movie.
        duration_time_in_minutes (str): The duration of the movie in minutes.
        age_rating (Rating): The age rating of the movie.
        imdb_rating (float): The movie's rating on IMDB.
        vote_count (int): The number of votes the movie has received.
        more_info_url (str): The URL for more information about the movie.
    """

    rank_position: int
    title: str
    poster_url: str
    release_year: int
    duration_time_in_minutes: str
    age_rating: AgeRating
    imdb_rating: float
    vote_count: int
    more_info_url: str

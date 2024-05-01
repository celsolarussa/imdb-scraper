import pytest
from bs4 import BeautifulSoup

from imdb_scraper.scraper.imdb_scraper import (
    AgeRating, _scrape, convert_age_rating_to_enum,
    convert_duration_time_to_integer, convert_votes_to_integer,
    get_li_tags_from_page)


def test_convert_votes_to_integer():
    assert convert_votes_to_integer('1M') == 1000000
    assert convert_votes_to_integer('1K') == 1000
    with pytest.raises(ValueError):
        convert_votes_to_integer('1B')


def test_convert_duration_time_to_integer():
    assert convert_duration_time_to_integer('2h 30m') == 150
    assert convert_duration_time_to_integer('2h') == 120
    assert convert_duration_time_to_integer('30m') == 30


def test_convert_age_rating_to_enum():
    assert convert_age_rating_to_enum('R') == AgeRating.R
    assert convert_age_rating_to_enum('PG-13') == AgeRating.PG13
    assert convert_age_rating_to_enum('UNKNOWN') == AgeRating.UNKNOWN


def test_get_li_tags_from_page():
    html = (
        html
    ) = """
    <html>
        <body>
            <ul class="ipc-metadata-list">
                <li>Item 1</li>
                <li>Item 2</li>
                <li>Item 3</li>
            </ul>
        </body>
    </html>
    """

    assert len(get_li_tags_from_page(html)) == 3
    assert all(tag.name == 'li' for tag in get_li_tags_from_page(html))


def test__scrape():
    html = """
    <li class="ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent"><div class="sc-e5a25b0f-0 jQjDIb cli-poster-container"><div class="ipc-poster ipc-poster--base ipc-poster--dynamic-width ipc-sub-grid-item ipc-sub-grid-item--span-2" role="group"><div aria-label="add to watchlist" class="ipc-watchlist-ribbon ipc-focusable ipc-watchlist-ribbon--s ipc-watchlist-ribbon--base ipc-watchlist-ribbon--loading ipc-watchlist-ribbon--onImage ipc-poster__watchlist-ribbon" role="button" tabindex="0"><svg class="ipc-watchlist-ribbon__bg" height="34px" role="presentation" viewbox="0 0 24 34" width="24px" xmlns="http://www.w3.org/2000/svg"><polygon class="ipc-watchlist-ribbon__bg-ribbon" fill="#000000" points="24 0 0 0 0 32 12.2436611 26.2926049 24 31.7728343"></polygon><polygon class="ipc-watchlist-ribbon__bg-hover" points="24 0 0 0 0 32 12.2436611 26.2926049 24 31.7728343"></polygon><polygon class="ipc-watchlist-ribbon__bg-shadow" points="24 31.7728343 24 33.7728343 12.2436611 28.2926049 0 34 0 32 12.2436611 26.2926049"></polygon></svg><div class="ipc-watchlist-ribbon__icon" role="presentation"><svg class="ipc-loader ipc-loader--circle ipc-watchlist-ribbon__loader" data-testid="watchlist-ribbon-loader" height="48px" role="presentation" version="1.1" viewbox="0 0 48 48" width="48px" xmlns="http://www.w3.org/2000/svg"><g class="ipc-loader__container" fill="currentColor"><circle class="ipc-loader__circle ipc-loader__circle--one" cx="24" cy="9" r="4"></circle><circle class="ipc-loader__circle ipc-loader__circle--two" cx="35" cy="14" r="4"></circle><circle class="ipc-loader__circle ipc-loader__circle--three" cx="39" cy="24" r="4"></circle><circle class="ipc-loader__circle ipc-loader__circle--four" cx="35" cy="34" r="4"></circle><circle class="ipc-loader__circle ipc-loader__circle--five" cx="24" cy="39" r="4"></circle><circle class="ipc-loader__circle ipc-loader__circle--six" cx="13" cy="34" r="4"></circle><circle class="ipc-loader__circle ipc-loader__circle--seven" cx="9" cy="24" r="4"></circle><circle class="ipc-loader__circle ipc-loader__circle--eight" cx="13" cy="14" r="4"></circle></g></svg></div></div><div class="ipc-media ipc-media--poster-27x40 ipc-image-media-ratio--poster-27x40 ipc-media--base ipc-media--poster-m ipc-poster__poster-image ipc-media__img" style="width:100%"><img alt="Tim Robbins in The Shawshank Redemption (1994)" class="ipc-image" loading="lazy" sizes="50vw, (min-width: 480px) 34vw, (min-width: 600px) 26vw, (min-width: 1024px) 16vw, (min-width: 1280px) 16vw" src="https://m.media-amazon.com/images/M/MV5BNDE3ODcxYzMtY2YzZC00NmNlLWJiNDMtZDViZWM2MzIxZDYwXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_QL75_UX140_CR0,1,140,207_.jpg" srcset="https://m.media-amazon.com/images/M/MV5BNDE3ODcxYzMtY2YzZC00NmNlLWJiNDMtZDViZWM2MzIxZDYwXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_QL75_UX140_CR0,1,140,207_.jpg 140w, https://m.media-amazon.com/images/M/MV5BNDE3ODcxYzMtY2YzZC00NmNlLWJiNDMtZDViZWM2MzIxZDYwXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_QL75_UX210_CR0,2,210,311_.jpg 210w, https://m.media-amazon.com/images/M/MV5BNDE3ODcxYzMtY2YzZC00NmNlLWJiNDMtZDViZWM2MzIxZDYwXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_QL75_UX280_CR0,3,280,414_.jpg 280w" width="140"/></div><a aria-label="View title page for The Shawshank Redemption" class="ipc-lockup-overlay ipc-focusable" href="/title/tt0111161/?ref_=chttp_i_1"><div class="ipc-lockup-overlay__screen"></div></a></div></div><div class="ipc-metadata-list-summary-item__c"><div class="ipc-metadata-list-summary-item__tc"><span aria-disabled="false" class="ipc-metadata-list-summary-item__t"></span><div class="sc-b189961a-0 hBZnfJ cli-children"><div class="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN cli-title"><a class="ipc-title-link-wrapper" href="/title/tt0111161/?ref_=chttp_t_1" tabindex="0"><h3 class="ipc-title__text">1. The Shawshank Redemption</h3></a></div><div class="sc-b189961a-7 feoqjK cli-title-metadata"><span class="sc-b189961a-8 kLaxqf cli-title-metadata-item">1994</span><span class="sc-b189961a-8 kLaxqf cli-title-metadata-item">2h 22m</span><span class="sc-b189961a-8 kLaxqf cli-title-metadata-item">R</span></div><span class="sc-b189961a-1 kcfvgk"><div class="sc-e2dbc1a3-0 ajrIH sc-b189961a-2 fkPBP cli-ratings-container" data-testid="ratingGroup--container"><span aria-label="IMDb rating: 9.3" class="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating" data-testid="ratingGroup--imdb-rating"><svg class="ipc-icon ipc-icon--star-inline" fill="currentColor" height="24" role="presentation" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M12 20.1l5.82 3.682c1.066.675 2.37-.322 2.09-1.584l-1.543-6.926 5.146-4.667c.94-.85.435-2.465-.799-2.567l-6.773-.602L13.29.89a1.38 1.38 0 0 0-2.581 0l-2.65 6.53-6.774.602C.052 8.126-.453 9.74.486 10.59l5.147 4.666-1.542 6.926c-.28 1.262 1.023 2.26 2.09 1.585L12 20.099z"></path></svg>9.3<span class="ipc-rating-star--voteCount"> (<!-- -->2.9M<!-- -->)</span></span><button aria-label="Rate The Shawshank Redemption" class="ipc-rate-button sc-e2dbc1a3-1 jboOQc ratingGroup--user-rating ipc-rate-button--unrated ipc-rate-button--base" data-testid="rate-button"><span class="ipc-rating-star ipc-rating-star--base ipc-rating-star--rate"><svg class="ipc-icon ipc-icon--star-border-inline" fill="currentColor" height="24" role="presentation" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M22.724 8.217l-6.786-.587-2.65-6.22c-.477-1.133-2.103-1.133-2.58 0l-2.65 6.234-6.772.573c-1.234.098-1.739 1.636-.8 2.446l5.146 4.446-1.542 6.598c-.28 1.202 1.023 2.153 2.09 1.51l5.818-3.495 5.819 3.509c1.065.643 2.37-.308 2.089-1.51l-1.542-6.612 5.145-4.446c.94-.81.45-2.348-.785-2.446zm-10.726 8.89l-5.272 3.174 1.402-5.983-4.655-4.026 6.141-.531 2.384-5.634 2.398 5.648 6.14.531-4.654 4.026 1.402 5.983-5.286-3.187z"></path></svg><span class="ipc-rating-star--rate">Rate</span></span></button></div></span></div></div></div><div class="sc-10233bc-1 lkPiVh cli-post-element"><button aria-disabled="false" aria-label="See more information about The Shawshank Redemption" class="ipc-icon-button cli-info-icon ipc-icon-button--base ipc-icon-button--onAccent2" role="button" tabindex="0" title="See more information about The Shawshank Redemption"><svg class="ipc-icon ipc-icon--info" fill="currentColor" height="24" role="presentation" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M0 0h24v24H0V0z" fill="none"></path><path d="M11 7h2v2h-2zm0 4h2v6h-2zm1-9C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"></path></svg></button></div></li>
    """

    element = BeautifulSoup(html, 'html.parser').li
    card = _scrape(element)

    assert card.rank_position == 1
    assert card.title == 'The Shawshank Redemption'
    assert (
        card.poster_url
        == 'https://m.media-amazon.com/images/M/MV5BNDE3ODcxYzMtY2YzZC00NmNlLWJiNDMtZDViZWM2MzIxZDYwXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_QL75_UX140_CR0,1,140,207_.jpg'
    )
    assert card.release_year == 1994
    assert card.duration_time_in_minutes == 142
    assert card.age_rating == AgeRating.R
    assert card.imdb_rating == 9.3
    assert card.vote_count == 2900000
    assert card.more_info_url == 'https://www.imdb.com/title/tt0111161/?ref_=chttp_t_1'

from Vanime.api import Vanime
from re import match

api = Vanime()


def test_get_anime():
    get_anime_response = api.get_anime('black-lagoon')
    assert match(r'\n\s{4}-+\n(?:\s{4}\|.+\n){7,}\s{4}-+|recapcha', get_anime_response)

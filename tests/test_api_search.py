from Vanime.api import Vanime
from re import match

api = Vanime()


def test_search():
    search_response = api.search('black lagoon')
    assert match(r'\n\s{4}-+\n(?:\s{4}\|.+\n){4}\s{4}-+\n|recapcha', search_response)

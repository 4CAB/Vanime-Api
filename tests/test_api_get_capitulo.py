from Vanime.api import Vanime
from re import match

api = Vanime()


def test_search_without_check():
    get_capitulo_response = api.get_capitulo(slug='black-lagoon', numero='1', check=0)
    assert match(r'\n\s{4}-+\n(?:\s{4}\|.+\n)+\s|recapcha', get_capitulo_response)


def test_search_with_check():
    get_capitulo_response = api.get_capitulo(slug='black-lagoon', numero='1', check=1)
    assert match(r'\n\s{4}-+\n(?:\s{4}\|.+\n)+\s|recapcha', get_capitulo_response)

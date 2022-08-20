import cloudscraper
from requests import exceptions
from Vanime.utils import api_utils, formatters


class Vanime:
    def __init__(self):
        self.session = cloudscraper.CloudScraper()
        self.session.get("https://www3.animeflv.net/")

    def req(self, url, method='GET', data=None):
        """Hace los requests"""
        if method == 'GET':
            try:
                data = self.session.get(url).text
            except exceptions.ConnectionError:
                print('Ha ocurrido un error de conexión.\nReintentandolo')
                self.req(url, method, data)
            return data
        elif method == 'POST':
            return self.session.post(url, data=data)

    def search(self, value: str):
        """Busca animes segun el texto recibido"""
        data = self.req('https://www3.animeflv.net/api/animes/search',
                        data={'value': value}, method='POST')

        recapcha = api_utils.recapcha(data.text)
        if recapcha:
            return recapcha

        new_data = [{'Titulo': i['title'], 'Tipo': i['type'], 'Slug': i['slug'],
                     'Enlace': f"https://www3.animeflv.net/anime/{i['slug']}"
                     } for i in data.json()]

        return formatters.formatter_list(new_data)

    def get_anime(self, slug: str):
        """Obtiene informacion de los animes por medio del slug"""
        data = self.req(f'https://www3.animeflv.net/anime/{slug}')

        recapcha = api_utils.recapcha(data)
        if recapcha:
            return recapcha

        data = api_utils.get_anime_info(data)
        data['Enlace'] = f'https://www3.animeflv.net/anime/{slug}'
        return formatters.anime_info_formatter(data)

    def get_capitulo(self, slug: str, numero: str, check: bool):
        """Obtiene los enlaces para ver el capitulo"""
        data = self.req(f'https://www3.animeflv.net/ver/{slug}-{numero}')

        recapcha = api_utils.recapcha(data)
        if recapcha:
            return recapcha

        content = api_utils.get_caps(response=data, check=check)

        return formatters.capitulo_info_formatter(content)

import cloudscraper
from requests import exceptions
from Vanime.utils import api_utils, formatters


class Vanime:
    def __init__(self):
        self.session = cloudscraper.CloudScraper()
        self.session.get("https://www3.animeflv.net/")

    def search(self, value: str):
        """Busca animes segun el texto recibido"""
        try:
            data = self.session.post('https://www3.animeflv.net/api/animes/search',
                                     data={'value': value})
        except exceptions.JSONDecodeError:
            self.search()

        content = ""
        for i in data.json():
            content += f"""
    ------------------------
    |Titulo: {i['title']}
    |Slug: {i['slug']}
    |Tipo: {i['type']}
    |Enlace: https://www3.animeflv.net/anime/{i['slug']}
    ------------------------\n"""

        return content

    def get_anime(self, slug: str):
        """Obtiene informacion de los animes por medio del slug"""
        try:
            data = self.session.get(f'https://www3.animeflv.net/anime/{slug}').text
        except exceptions.ConnectionError:
            print('Ha ocurrido un error de conexión.\nReintentandolo')
            data = self.session.get(f'https://www3.animeflv.net/anime/{slug}').text

        recapcha = api_utils.recapcha(data)
        if recapcha:
            return recapcha

        data = api_utils.get_anime_info(data)
        data['Enlace'] = f'https://www3.animeflv.net/anime/{slug}'
        return formatters.anime_info_formatter(data)

    def get_capitulo(self, slug: str, numero: str, check: bool):
        """Obtiene los enlaces para ver el capitulo"""
        try:
            data = self.session.get(f'https://www3.animeflv.net/ver/{slug}-{numero}').text
        except exceptions.ConnectionError:
            print('Ha ocurrido un error de conexión.\nReintentandolo')
            data = self.session.get(f'https://www3.animeflv.net/ver/{slug}-{numero}').text

        recapcha = api_utils.recapcha(data)
        if recapcha:
            return recapcha

        content = api_utils.get_caps(response=data, check=check)

        return formatters.capitulo_info_formatter(content)

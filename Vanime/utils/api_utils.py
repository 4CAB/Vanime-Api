from bs4 import BeautifulSoup, element
from re import findall as refind
from json import loads as jloads
import cloudscraper
from .formatters import formatter


def recapcha(data):
    """Verifica si ha saltado el repcacha."""
    if "<title>Verifica que no eres un bot | AnimeFLV</title>" in data:
        return formatter(data="Ha saltado el recapcha, espera unos segundos")


def get_anime_info(response: str):
    """Extrae los datos del anime y les da un formato."""
    soup = BeautifulSoup(response, 'lxml')
    image = soup.find('meta', property='og:image')['content']
    title = soup.find('h1', class_='Title').string
    genres = []

    if "Anime Single Bglg" in response:
        content = soup.find('article', class_='Anime Single Bglg')
        status = content.find('strong', class_=['Anm-Off', 'Anm-On']).string
        description = content.find_all(['p', 'a'])[1].get_text().replace('Sinopsis: ', '')
        episodes = soup.find_all('li', class_='Episode')[-1]
        episodes = episodes.string.split()[-1]

        for i in content.find_all('a', class_='Tag'):
            genres.append({i.string: i['href']})

    else:
        status = soup.find('span', class_='fa-tv').string
        description = soup.find('div', class_='Description').get_text()
        episodes = refind(r'var episodes = (.*);', response)[0]
        episodes = refind(r'\[(\d+),', episodes)[0]

        for i in soup.find('nav', class_='Nvgnrs'):
            if isinstance(i, element.Tag):
                genres.append({i.string: i['href']})

    data = {'Titulo': title,
            'Imagen': image,
            'Status': status,
            'Sipnosis': description.replace('\n', ''),
            'Capitulos': episodes,
            'Generos': genres}

    return data


def get_caps(response: str, check: bool = False):
    """Extrae los datos de los capitulos y les da un formato."""
    data = jloads(refind(r'var videos = ({.*});', response)[0])
    new_data = []

    for i in data['SUB']:
        if check:
            if check_status_link(i['code']):
                continue
        new_data.append({'Titulo': i['title'], 'Anuncios': i['ads'], 'Enlace': i['code']})

    return new_data


def check_status_link(link):
    """Check if links work"""
    dont_work_references = [
        'Not Found', 'Video not found!', 'Sorry this video is unavailable: DMCA Takedown',
        'Content Restricted', 'COPYRIGHTS_RESTRICTED']

    # check status link mega
    if "mega.nz" in link:
        data = [{"a": "g", "p": link.split("!")[1]}]
        link = 'https://g.api.mega.co.nz/cs?id=0&domain=meganz&v=2&lang=en'
        status_code, response = requests(link, method='POST', data=data)
        return 'err' in response
    else:
        status_code, response = requests(link)

    if status_code != 200:
        pass

    return any(_ in response for _ in dont_work_references)


def requests(link: str, method: str = 'GET', data: dict = None):
    scraper = cloudscraper.create_scraper()

    if method == 'POST':
        response = scraper.post(link, json=data)
    else:
        response = scraper.get(link)

    return response.status_code, response.text

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simp_get(url):

    try:
        with closing(get(url, stream=True)) as resp:
            content_type = resp.headers['Content-Type'].lower()
            if resp.status_code == 200 and content_type and content_type.find('html') > -1:
                return resp.content
            else:
                return None
    
    except RequestException as e:
        print("Error during request to {}: {}".format(url, str(e)))
        return None

soup = BeautifulSoup(simp_get("https://www.crunchyroll.com/videos/anime/popular"), 'html.parser')

shows = []

for a in soup.select('a'):
    if a.get('token') == 'shows-portraits':
        shows.append(a)

for show in shows:
    x, y, z = list(map(str.strip, show.text.strip().split('\n')))
    print("{}: {}\nHere's the link! {}".format(x, z, "https://www.crunchyroll.com" + show.get('href')))
    # print(list(map(str.strip, show.text.strip().split('\n'))))
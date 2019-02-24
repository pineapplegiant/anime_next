import requests
from bs4 import BeautifulSoup

soup = requests.get("https://www.crunchyroll.com/videos/anime")

 # Check to see if things work here
#print(result.status_code)

src = soup.content
print(src) # The whole damn site

soup.find_all("title")

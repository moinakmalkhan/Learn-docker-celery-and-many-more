from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")


bs = BeautifulSoup(html.read(), "lxml")
print(bs.find_all("span", {"class": "green"}))

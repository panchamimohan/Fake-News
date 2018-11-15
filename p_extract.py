from bs4 import BeautifulSoup
import urllib

url = urllib.urlopen('http://meinparlament.diepresse.com/')
content = url.read()
soup = BeautifulSoup(content, 'lxml')

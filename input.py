import urllib
from bs4 import BeautifulSoup
link = "https://www.geeksforgeeks.org/java-how-to-start-learning-java/"
f = urllib.urlopen(link)
myfile = f.read()
soup = BeautifulSoup(myfile,"html.parser")
page = soup.find_all('p')
print(type(page))
paragraphs = []
for x in page:
    paragraphs.append(str(x))
cleantext = BeautifulSoup(paragraphs[0], "lxml").text
print(cleantext)

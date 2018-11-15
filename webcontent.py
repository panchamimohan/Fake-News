import urllib
from bs4 import BeautifulSoup

#link = "https://www.americanmeadows.com/the-wild-roses"
#f = urllib.urlopen(link)
#html = f.read()

#print(myfile)
soup = BeautifulSoup(urllib.urlopen('https://www.americanmeadows.com/the-wild-roses').read())

for post in soup.find("p"):
    print post

#for x in soup.find("div", "class2"):
#    print x 

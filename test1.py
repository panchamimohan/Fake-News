import urllib2
response = urllib2.urlopen('http://en.wikipedia.org/')
html = response.read()
print html

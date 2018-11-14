import wikipedia
search = wikipedia.search("nellika")


print(search)
for p in search:
    pp = wikipedia.page(p)
    print(pp.content)


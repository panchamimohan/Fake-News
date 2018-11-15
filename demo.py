try: 
	import wikisearch
	import newask
	from googlesearch import search 
	import wikipedia
except ImportError: 
	print("No module named 'google' found") 

query = "taj mahal"

def check(j):
	if "en.wikipedia.org" in j:
		return 1
	elif "www.youtube.com" in j:
	        return 2
	else :
        	return 0
            


for j in search(query, tld="co.in", num=2, stop=1, pause=2):
	res = check(j)
	if res==1:
		wikisearch.process(query)
		newask.process("search_results.txt")
    	
    #f.write(j)
    #f.write("\n")



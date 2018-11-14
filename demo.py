try: 
	from googlesearch import search 
	import wikipedia
except ImportError: 
	print("No module named 'google' found") 

# to search 
query = "lulu mall"
f= open("search_results.txt","w")

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
    	try:
    		search = wikipedia.search(query)
    		for p in search:
    			pp = wikipedia.page(p)
    			f.write(pp.content.encode('utf-8'))
	except wikipedia.exceptions.DisambiguationError as e:
   		 print("Error: {0}".format(e))
	
    #f.write(j)
    #f.write("\n")
f.close() 


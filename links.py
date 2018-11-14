
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
query = "modi president"
f= open("search_links.txt","w")
  
for j in search(query, tld="co.in", num=5, stop=1, pause=2): 
    f.write(j)
    f.write("\n")


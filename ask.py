import os, sys, errno
import subprocess
import re
import itertools
import nltk
from nltk.stem import PorterStemmer
import bs4

sys.path.append("modules")
import questionContentSelector
import questionFromSentence
import coref

if __name__ == '__main__':
  path_to_article = sys.argv[1]
  num_questions = int(sys.argv[2])
  #try: 
	 #from googlesearch import search 
 # except ImportError: 
	 #print("No module named 'google' found") 

# to search 
 #query = "Geeksforgeeks"

 # #for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
	 #print(j) 

  article_content = coref.process(path_to_article)

  selected_content = questionContentSelector.process(article_content)

  questions = questionFromSentence.process(selected_content)

  questions = questions[:num_questions]
  for question in questions:
    print(question + "\n")


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
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def process(path_to_article):
  #path_to_article = open("search_results.txt","r")
  #path_to_article = sys.argv[1]
  num_questions = 5
  f= open("ques.txt","w")

  article_content = coref.process(path_to_article)

  selected_content = questionContentSelector.process(article_content)

  questions = questionFromSentence.process(selected_content)

  questions = questions[:num_questions]
  for question in questions:
    f.write(question+"\n")
  f.close()
  #path_to_article.close()


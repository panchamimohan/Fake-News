#!/usr/bin/python

# answer
# 11-411 NLP Spring 2013, Group 6

# To run, type ./answer article_name
# e.g. ./answer

# Useful tools which should be pre-installed
import os, sys, errno
import subprocess
import re
import itertools
import nltk
from nltk.stem import PorterStemmer
from bs4 import BeautifulSoup
# Import our modules from /modules
sys.path.append("modules")
import questionClassifier
import sourceContentSelector
import coref
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# To answer yes/no question, we want to just answer yes or no,
# and not returna  whole sentence. We do this by checking for
# any negatives in the sentence.
def contains_negative(sent):
  return "no" in sent or "not" in sent or "n't" in sent

# Answers a question from the information in article.
# Ranks all the sentences and then returns the top choice.
def answer(question, article):
    question = question.strip().rstrip("?").lower()
    question_type = questionClassifier.process(question)
    question = nltk.tokenize.word_tokenize(question)
    relevant = sourceContentSelector.getScoredSentences(question, article)
    top = max(relevant, key = lambda s: s[1])
    if question_type == "BOOLEAN":
      if contains_negative(top): return "No"
      else: return "Yes"
    else: return top[0]

# The main script
if __name__ == '__main__':
  article_name = sys.argv[1]
  questions = open(sys.argv[2]).read().split("\n")

  article = coref.process(article_name)
  for question in questions:
    print answer(question, article)

  #verbose = False
  #if (len(sys.argv) > 2):
  #  print("verbose?")
  #  if (sys.argv[2] =="--v" or sys.argv[2] == "-v"):
  #    verbose = True
  #
  #for year in ("S08", "S09", "S10"):
  #  if verbose:
  #    print "Year:", year
  #  prefix = "Question_Answer_Dataset_v1.1/"+year+"/"
  #  question_answer_pairs = open(prefix+"question_answer_pairs.txt").readlines()
  #  question_answer_pairs.pop(0)
  #  for line in question_answer_pairs:
  #    if not line.startswith(article_name): continue
  #    line = line.lstrip(article_name)
  #    end = line.find("?")
  #    if end == -1: continue
  #    question = line[:end+1].strip()
  #    line = line[end+1:].split()
  #    path_to_article = prefix+line.pop()+".txt"
  #    difficulty_answerer = line.pop()
  #    difficulty_questioner = line.pop()
  #    correct_answer = " ".join(line)
  #
  #    if verbose:
  #      print "Question:", question
  #      print "Difficulty from answerer:", difficulty_answerer
  #      print "Difficulty from questioner:", difficulty_questioner
  #
  #    article = coref.process(path_to_article)
  #
  #    if verbose:
  #      print "Our answer:", answer(question, article)
  #      print "Correct answer:", correct_answer
  #    else:
  #      print answer(question, article)

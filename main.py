import numpy as np
import pandas as pd
from IPython.display import display # Allows the use of display() for DataFrames
import matplotlib.pyplot as plt
import matplotlib
from parse import *
from datetime import datetime
import nltk
import os

text_ham = {}
text_spam = {}

def run():
	for root, dirs, files in os.walk("enron1/ham/"):
		for name in files:
			path = os.path.join(root, name)
			if os.path.isfile(path):
				txt = open(path,"r")
				inputs = txt.read()
				words = inputs.split()
				for word in words:
					if text_ham.get(word) != None:
						text_ham[word] = text_ham[word] + 1
					else:
						text_ham[word] = 1
				txt.close()
		print 'Number of hams:', len(files)
	for root, dirs, files in os.walk("enron1/spam/"):
		for name in files:
			path = os.path.join(root, name)
			if os.path.isfile(path):
				txt = open(path,"r")
				inputs = txt.read()
				words = inputs.split()
				for word in words:
					if text_spam.get(word) != None:
						text_spam[word] = text_spam[word] + 1
					else:
						text_spam[word] = 1
				txt.close()
		print 'Number of spams:', len(files)
	# print text_ham
	# print text_spam
	print 'Finish detection'

if __name__ == '__main__':
    run()
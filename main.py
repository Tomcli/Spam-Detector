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
		for i, name in enumerate(files):
			if i == 1500:
				break
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
		for i, name in enumerate(files):
			if i == 1500:
				break
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
	ham_frame = pd.DataFrame(text_ham.items(), columns=['Word', 'H_Frequency'])
	#ham_frame['ham'] = pd.Series(1, index=ham_frame.index)
	spam_frame = pd.DataFrame(text_spam.items(), columns=['Word', 'S_Frequency'])
	#spam_frame['ham'] = pd.Series(0, index=spam_frame.index)
	data = pd.merge(ham_frame,spam_frame, on='Word')
	data = data.loc[data['Word'].str.isalpha()]
	data = data.loc[data['Word'].str.len() > 1] 
	new_data = data.loc[(data['H_Frequency'] >= 300) ^ (data['S_Frequency'] >= 300)]
	print new_data
	print 'Finish detection'

if __name__ == '__main__':
    run()
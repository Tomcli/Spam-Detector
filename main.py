import numpy as np
import pandas as pd
from IPython.display import display # Allows the use of display() for DataFrames
import matplotlib.pyplot as plt
import matplotlib
from parse import *
from datetime import datetime
import nltk
import os
from sklearn.feature_extraction.text import CountVectorizer

text_ham = {}
text_spam = {}

#def data_frame(files, ham):

# text = pd.DataFrame({'text': [], 'class': []})
# text = text.append(data_frame("enron1/ham/", "ham"))
# text = text.append(data_frame("enron1/spam/", "spam"))
# print text

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
						text_ham[word.lower()] = text_ham[word.lower()] + 1
					else:
						text_ham[word.lower()] = 1
				txt.close()
		# print 'Number of hams:', len(files)
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
						text_spam[word.lower()] = text_spam[word.lower()] + 1
					else:
						text_spam[word.lower()] = 1
				txt.close()
		# print 'Number of spams:', len(files)
	# print text_ham
	# print text_spam
	ham_frame = pd.DataFrame(text_ham.items(), columns=['Word', 'H_Frequency'])
	#ham_frame['ham'] = pd.Series(1, index=ham_frame.index)
	spam_frame = pd.DataFrame(text_spam.items(), columns=['Word', 'S_Frequency'])
	#spam_frame['ham'] = pd.Series(0, index=spam_frame.index)
	data = pd.merge(ham_frame,spam_frame, on='Word')
	data = data.loc[(data['Word'].str.isalpha()) & (data['Word'].str.len() > 1)]
	new_data = data.loc[(data['H_Frequency'] >= 300) ^ (data['S_Frequency'] >= 300)]
	new_data['H-S'] = pd.Series((new_data.H_Frequency - new_data.S_Frequency)/1500., index=new_data.index)
	data_dic = {}
	for da in new_data.index:
		data_dic[new_data.loc[da,'Word']] = new_data.loc[da,'H-S']
	h_count = 0
	sp_count = 0
	for root, dirs, files in os.walk("enron2/ham/"):
		for i, name in enumerate(files):
			path = os.path.join(root, name)
			if os.path.isfile(path):
				txt = open(path,"r")
				inputs = txt.read()
				words = inputs.split()
				score = 0
				for word in words:
					if data_dic.get(word.lower()) != None:
						score+= data_dic[word.lower()]
				if score >= 0:
					h_count+=1
				txt.close()
		print 'Number of testing hams:', len(files)
		print 'Correctness:', float(h_count)/len(files)
	for root, dirs, files in os.walk("enron2/spam/"):
		for i, name in enumerate(files):
			path = os.path.join(root, name)
			if os.path.isfile(path):
				txt = open(path,"r")
				inputs = txt.read()
				words = inputs.split()
				score = 0
				for word in words:
					if data_dic.get(word.lower()) != None:
						score+= data_dic[word.lower()]
				if score < 0:
					sp_count+=1
				txt.close()
		print 'Number of testing spams:', len(files)
		print 'Correctness:', float(sp_count)/len(files)
	print 'Finish detection method 1'

	#count_vectorizer = CountVectorizer()
	#counts = count_vectorizer.fit_transform(text['text'].values)
	#print counts

	# english_vocab = set(w.lower() for w in nltk.corpus.words.words())
	# english = [x for x in english_vocab]
	# print len(english)

if __name__ == '__main__':
    run()
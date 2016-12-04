# Spam-Detector (In Progress)
Spam detector using natural learning processing. 

Training data are from **Enron-Spam**. 

##How to use

1. Run `python main.py` to train the classifier.

##Method 1

Create a spam filter based on the word frequency. We score each mail with the score for some certain keywords based on our training data.

Result: This filter generally has 15% to 20% error rate which is good for a simple method.

##Method 2

Create a spam filter based on the word frequency grouped by feature with machine learning classifier. We score each mail by the word frequency based on our training data. Then we will create a spam classifier with random forest/support vector machine based on the word frequency.
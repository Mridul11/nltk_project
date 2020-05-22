import nltk 
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 

ps = PorterStemmer()

example_words = ["python", "pythoner", "pythoning", "pythonicness"]
new_text = "It is very important to be pythonly while you are pythoning with python and pythonicness is amazingly awesome in a python way!"
words = word_tokenize(new_text)

def running():
    for w in words:
        print(ps.stem(w))

import nltk
from nltk import word_tokenize
text = "I love coding in Python."
tokens = word_tokenize(text)
tags = nltk.pos_tag(tokens, tagset = "universal")
print(tags)
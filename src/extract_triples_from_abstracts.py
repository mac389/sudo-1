import nltk
import pandas as pd 


from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from collections import Counter 

def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return ''


wordnet_lemmatizer = WordNetLemmatizer()

abstracts = open('./abstract_text.txt').read()

tagged = pos_tag(word_tokenize(abstracts))

tagged = [(word,get_wordnet_pos(pos)) for word,pos in tagged]

only_SVO = [(wordnet_lemmatizer.lemmatize(word,pos=pos),pos) for word,pos in tagged if pos in [wordnet.NOUN,wordnet.VERB]]

df = pd.DataFrame([{"word":word,"pos":pos,"count":count} for (word,pos),count in dict(Counter(only_SVO)).iteritems()],
					columns=["word","pos","count"])

df.to_csv('../data/words.csv',index=False)

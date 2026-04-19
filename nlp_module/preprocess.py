import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer

def download_resources():
    resources = [
        ('tokenizers/punkt', 'punkt'),
        ('corpora/stopwords', 'stopwords'),
        ('corpora/wordnet', 'wordnet'),
        ('taggers/averaged_perceptron_tagger_eng', 'averaged_perceptron_tagger_eng')
    ]

    for path,name in resources:
        try:
            nltk.data.find(path)
        except:
            nltk.download(name)

download_resources()

stopword = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def pre_process(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]','',text)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stopword]

    pos_tags = nltk.pos_tag(tokens)

    tokens = [lemmatizer.lemmatize(word, get_wordnet_pos(tag)) for word,tag in pos_tags]

    cleaned_text = " ".join(tokens)

    return cleaned_text
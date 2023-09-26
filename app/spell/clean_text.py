import nltk.corpus
nltk.download('stopwords')
from nltk.corpus import stopwords
from .conf import LANGUAGE

def clean_stopwords(text: str)->str:
    """Remove stop words and return key words

    Args:
        text (str): text to be cleaned

    Returns:
        str: key words
    """
    stop = stopwords.words(LANGUAGE)
    text = " ".join([word for word in text.split() if word not in (stop)])

    return text
import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

def language_detector(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Count the number of stopwords in each sentence for each language
    english_stopwords = set(stopwords.words('english'))
    french_stopwords = set(stopwords.words('french'))
    spanish_stopwords = set(stopwords.words('spanish'))

    english_count = 0
    french_count = 0
    spanish_count = 0

    for sentence in sentences:
        words = word_tokenize(sentence.lower())
        english_count += len([word for word in words if word in english_stopwords])
        french_count += len([word for word in words if word in french_stopwords])
        spanish_count += len([word for word in words if word in spanish_stopwords])

    # Determine which language has the highest count of stopwords
    lang = 'Unknown'
    if english_count > french_count and english_count > spanish_count:
        lang = 'English'
    elif french_count > english_count and french_count > spanish_count:
        lang = 'French'
    elif spanish_count > english_count and spanish_count > french_count:
        lang = 'Spanish'

    return lang



text = "My Name is Phill"
lang = language_detector(text)
print(lang)

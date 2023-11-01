"""Utilities for topic modeling"""

from gensim.corpora import Dictionary
from gensim.models import LdaModel
import nltk

def extract_topics_from_documents(documents):
    """
    Extract topics from a list of documents
    """

    nltk.download('punkt')
    tokenized_data = [nltk.word_tokenize(doc.page_content.lower()) for doc in documents]
    dictionary = Dictionary(tokenized_data)
    corpus = [dictionary.doc2bow(text) for text in tokenized_data]
    lda_model = LdaModel(corpus, num_topics=50, id2word=dictionary, passes=15)
    topics = lda_model.print_topics(num_words=4)

    for topic in topics:
        print(f"Topic {topic[0]}: {topic[1]}")

    return topics

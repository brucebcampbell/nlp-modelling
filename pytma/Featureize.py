from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split


class Featurize():
    """
    Class for featurizing text.  BOW, tf-idf, vector embeddings
    """

    def __init__(self, text):
        self.text = text

    # Term Frequency(TF) is the count the number of words occurred in each document.
    # The main issue with Term Frequency is that it will give more weight to longer documents.
    # Term Frequency is the BoW model.
    # IDF(Inverse Document Frequency) measures the amount of information a given word provides
    # across the document. IDF is the logarithmically scaled inverse ratio of the number of
    # documents that contain the word and the total number of documents
    def tf_idf(self):
        tf = TfidfVectorizer()
        text_tf = tf.fit_transform(self.text.split())
        return text_tf

    def tf(self):
        # tokenizer to remove unwanted elements from out data like symbols and numbers
        token = RegexpTokenizer(r'[a-zA-Z0-9]+')
        #stop_words : string {‘english’}, ‘english’is a built-in stop word list for English .
        # There are several known issues with ‘english’ and we should consider an alternative
        cv = CountVectorizer(lowercase=True, stop_words='english', ngram_range=(1, 1), tokenizer=token.tokenize)
        text_counts = cv.fit_transform(self.text.split())
        return text_counts


if __name__ == '__main__':
    # This will be the unit test
    test_text = "He received multiple nominations for Nobel Prize in Literature every year from 1902 to 1906, \
     and nominations for Nobel Peace Prize in 1901, 1902 and 1910, and his miss of the prize is a major Nobel \
     prize controversy.[3][4][5][6] Born to an aristocratic Russian family in 1828,[2] he is best known for \
      the novels War and Peace (1869) and Anna Karenina (1877),[7] often cited as pinnacles of realist fiction. \
    [2] He first achieved literary acclaim in his twenties with his semi-autobiographical trilogy,  \
    Childhood, Boyhood, and Youth (1852–1856), and Sevastopol Sketches (1855), based upon his experiences \
    in the Crimean War."
    feat = Featurize(test_text)

    text_tf = feat.tf()
    print(text_tf)

    print(len(test_text.split()))
    print(len(set(test_text.split())))


    text_tf_idf = feat.tf_idf()
    print(text_tf_idf)

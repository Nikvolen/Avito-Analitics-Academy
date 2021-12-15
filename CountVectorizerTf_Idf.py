from math import log
from pprint import pprint


class CountVectorizer:
    def __init__(self):
        self.vocabulary = []
        self.term_doc_matrix = []

    def fit_transform(self, raw_documents: list) -> list:
        """
        Learn the vocabulary dictionary and return document-term matrix.
        :param raw_documents: List of strings
        :return: term-document matrix
        """
        for doc in raw_documents:
            doc = doc.lower().split()
            word_dict = dict.fromkeys(self.vocabulary, 0)
            for word in doc:
                word_dict[word] = word_dict.setdefault(word, 0) + 1

            self.vocabulary = list(word_dict.keys())
            self.term_doc_matrix.append(list(word_dict.values()))

        for vector in self.term_doc_matrix:
            vector.extend([0, ] * (len(self.vocabulary) - len(vector)))

        return self.term_doc_matrix

    def get_feature_names(self) -> list:
        """
        Array mapping from feature integer indices to feature name.
        :return: A list of feature names.
        """
        return self.vocabulary


class TfidfTransformer:
    def __init__(self):
        self.tf_matrix = []
        self.idf_matrix = []
        self.tfidf_matrix = []

    def tf_transform(self, count_matrix: list) -> list:
        if len(count_matrix) > 0:
            for text in count_matrix:
                res = []
                length = sum(text)
                for elem in text:
                    res.append(round(elem / length, 3))
                self.tf_matrix.append(res)
        return self.tf_matrix

    def idf_transform(self, count_matrix: list) -> list:
        if len(count_matrix) > 0:
            count_docs = len(count_matrix)
            for i, _ in enumerate(count_matrix[0]):
                docs_with_word = 0
                for doc in count_matrix:
                    if doc[i] > 0:
                        docs_with_word += 1
                self.idf_matrix.append(round(log((count_docs + 1) / (docs_with_word + 1)) + 1, 3))
        return self.idf_matrix

    def fit_transform(self, count_matrix: list) -> list:
        self.tf_transform(count_matrix)
        self.idf_transform(count_matrix)
        for row, _ in enumerate(count_matrix):
            res = []
            for col, _ in enumerate(count_matrix[0]):
                res.append(round(self.tf_matrix[row][col] * self.idf_matrix[col], 3))
            self.tfidf_matrix.append(res)
        return self.tfidf_matrix


class TfidfVectorizer(CountVectorizer):
    def __init__(self):
        super().__init__()
        self.tfidf_transformer = TfidfTransformer()
        self.tfidf_matrix = []
        self.matrix = []

    def fit_transform(self, raw_documents: list) -> list:
        self.matrix = super().fit_transform(raw_documents)
        self.tfidf_matrix = self.tfidf_transformer.fit_transform(self.matrix)
        return self.tfidf_matrix


if __name__ == '__main__':
    corpus = ['Crock Pot Pasta Never boil pasta again',
               'Pasta Pomodoro Fresh ingredients Parmesan to taste',
               'pasta pasta Pasta PASTA paSTa pasta']

    print('Задание 1: count vectorizer')
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    pprint(count_matrix)
    print('\n')

    print('Задание 2: term frequency')
    transformer = TfidfTransformer()
    tf_matrix = transformer.tf_transform(count_matrix)
    pprint(tf_matrix)
    print('\n')

    print('Задание 3: inverse document-frequency')
    transformer = TfidfTransformer()
    idf_matrix = transformer.idf_transform(count_matrix)
    print(idf_matrix)
    print('\n')

    print('Задание 4: tf-idf transformer')
    transformer = TfidfTransformer()
    tfidf_matrix = transformer.fit_transform(count_matrix)
    pprint(tfidf_matrix)
    print('\n')

    print('Задание 5: tf-idf vectorizer')
    vectorizer = TfidfVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    pprint(count_matrix)



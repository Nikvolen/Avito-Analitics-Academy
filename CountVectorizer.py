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
        word_dict = {}
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


if __name__ == '__main__':
    corpus = ['Crock Pot Pasta Never boil pasta again',
              'Pasta Pomodoro Fresh ingredients Parmesan to taste',
              'pasta pasta Pasta PASTA paSTa pasta']

    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    assert vectorizer.get_feature_names() == ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro', 'fresh',
                                              'ingredients', 'parmesan', 'to', 'taste']
    for vector in count_matrix:
        print(vector)


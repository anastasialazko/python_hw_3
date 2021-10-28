from collections import Counter


class CountVectorizer():
    def __init__(self):
        self.feature_names = set()

    def fit(self, corpus) -> list:
        splitted_sentences = []
        for sentence in corpus:
            splitted_sentence = sentence.lower().split()
            for word in splitted_sentence:
                self.feature_names.add(word)
            splitted_sentences.append(splitted_sentence)
        return splitted_sentences

    def transform(self, corpus) -> list:
        matrix = []
        for sentence in self.fit(corpus):
            count_words_in_sentence = []
            counter = Counter(sentence)
            for word in self.feature_names:
                count_words_in_sentence.append(counter.get(word, 0))
            matrix.append(count_words_in_sentence)
        return matrix

    def fit_transform(self, corpus):
        return self.transform(corpus)

    def get_feature_names(self) -> set:
        return self.feature_names


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)

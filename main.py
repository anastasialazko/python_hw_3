class CountVectorizer():
    def __init__(self):
        self.feature_names = {}
        self.count_matrix = []

    def fit_transform(self, corpus: list) -> []:
        index = 0
        for sentence in corpus:
            for word in sentence.lower().split():
                if word not in self.feature_names:
                    self.feature_names[word] = index
                    index += 1

        for sentence in corpus:
            count_words = [0] * len(self.feature_names)
            for word in sentence.lower().split():
                count_words[self.feature_names[word]] += 1
            self.count_matrix.append(count_words)

        return self.count_matrix

    def get_feature_names(self) -> []:
        return list(self.feature_names.keys())


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
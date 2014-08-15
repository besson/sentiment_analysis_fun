class SentimentScorer:

    def __init__(self, _sentiment_file):
        self.__scores = self._sentiment_scores(_sentiment_file)

    def scores(self):
        return self.__scores

    def _sentiment_scores(self, _file):
        sentiments = open(_file)
        scores = {}

        for word in sentiments:
            term, score = word.split("\t")
            scores[term] = int(score)

        sentiments.close()

        return scores

    def calculate_score(self, line):
        _sum = 0
        for word in line.split("\t")[2].split():
            if (word in self.__scores):
                _sum += self.__scores[word]

        return _sum

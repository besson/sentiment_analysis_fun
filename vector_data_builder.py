import sys
from sentiment_scorer import SentimentScorer


class VectorDataBuilder:

    def __init__(self, sentiment_file):
        self.__scores = SentimentScorer(sentiment_file).scores()
        self.__writer = open("review_features.csv", "wb")

    def get_vectors(self, sample_file):
        sample_file = open(sample_file)

        header = ""
        for i in range(len(self.__scores.keys())):
            header += ("'%s'," % str(i))
        header += "'class'\n"
        self.__writer.write(header)

        for line in sample_file:
            vector = ""

            for word in self.__scores.keys():
                if (str(word) in line.split("\t")[2]):
                    vector += "%d," % self.__scores[word]
                else:
                    vector += "0,"

            vector += "\'a%s\'," % str(line.split("\t")[3][0])
            vector = vector[0:-1]
            vector += "\n"
            self.__writer.write(vector)

        self.__writer.close()

if __name__ == '__main__':
    VectorDataBuilder(sys.argv[1]).get_vectors(sys.argv[2])

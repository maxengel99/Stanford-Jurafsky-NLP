class NaiveBayes():
    @staticmethod
    def get_word_prob(word, movie_data_info, sentiment):
        if word not in movie_data_info["unique_words"]:
            return -1
        
        if sentiment == "N":
            if word not in movie_data_info["word_neg_prob"]:
                return 1 / movie_data_info["word_neg_count"].get(word, 0) + \
                            movie_data_info["word_pos_count"].get(word, 0) + \
                            len(movie_data_info["unique_words"])
            return movie_data_info["word_neg_prob"][word]
        else:
            if word not in movie_data_info["word_pos_prob"]:
                return 1 / movie_data_info["word_pos_count"].get(word, 0) + \
                            movie_data_info["word_pos_count"].get(word, 0) + \
                            len(movie_data_info["unique_words"])
            return movie_data_info["word_pos_prob"][word]

    @staticmethod
    def get_pred(phrase, movie_data_info, sentiment):
        parsed_words = phrase.split(" ")
        prob_list = []
        for word in parsed_words:
            prob = NaiveBayes.get_word_prob(word, movie_data_info, sentiment)
            if prob == "-1":
                continue
            
            prob_list.append(prob)
        
        prob = 1
        for elem in prob_list:
            prob = prob * elem
        return prob
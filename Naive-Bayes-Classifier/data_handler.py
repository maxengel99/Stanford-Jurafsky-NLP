import pandas as pd

class DataHandler():

    @staticmethod
    def read_and_clean_data():
        movie_training_dataTSV = './Data/train.tsv'

        movie_training_df = pd.read_csv(movie_training_dataTSV, sep='\t')
        movie_training_df.drop("PhraseId", axis=1, inplace=True)
        movie_training_df.drop("SentenceId", axis=1, inplace=True)
        movie_training_df = movie_training_df[movie_training_df.Sentiment != 2]
        movie_training_df["Sentiment"].replace({0: "N", 1: "N", 3: "P", 4: "P"}, inplace=True)
        movie_training_df["Phrase"] = movie_training_df["Phrase"].str.lower()
        movie_training_df["Phrase"] = movie_training_df["Phrase"].str.replace(",    ", "")
        movie_training_df["Phrase"] = movie_training_df["Phrase"].str.replace("  ", " ")
        movie_training_df.reset_index(drop=True, inplace=True)

        return movie_training_df

    @staticmethod
    def create_train_validation_sets(movie_df):
        movie_train = movie_df.sample(frac=0.8, random_state = 200)
        movie_validation = movie_df.drop(movie_train.index)

        return movie_train, movie_validation
    
    
    @staticmethod
    def get_counts(movie_training_df):
        '''Gets output counts + probability, word counts, union'''

        count_prob_object = {
            "neg_prob": 0,
            "pos_prob": 0,
            "unique_words": set(),
            "word_neg_count": {},
            "word_pos_count": {},
            "word_neg_prob": {},
            "word_pos_prob": {}
        }

        sentiment_count = movie_training_df.groupby("Sentiment").size()
        count_prob_object["neg_prob"] = sentiment_count["N"]/len(movie_training_df)
        count_prob_object["pos_prob"] = sentiment_count["P"]/len(movie_training_df)

        for _, row in movie_training_df.iterrows():
            parsed_words = row["Phrase"].split(" ")
            for word in parsed_words:
                count_prob_object["unique_words"].add(word)

                if row["Sentiment"] == "N":
                    if word not in count_prob_object["word_neg_count"]:
                        count_prob_object["word_neg_count"][word] = 1
                    else:
                        count_prob_object["word_neg_count"][word] += 1
                else:
                    if word not in count_prob_object["word_pos_count"]:
                        count_prob_object["word_pos_count"][word] = 1
                    else:
                        count_prob_object["word_pos_count"][word] += 1

        
        for word in count_prob_object["unique_words"]:
            count_prob_object["word_neg_prob"][word] = (count_prob_object["word_neg_count"].get(word, 0) + 1) \
                                                        / (count_prob_object["word_neg_count"].get(word, 0) + \
                                                            count_prob_object["word_pos_count"].get(word, 0) + \
                                                            len(count_prob_object["unique_words"]))
            count_prob_object["word_pos_prob"][word] = (count_prob_object["word_pos_count"].get(word, 0) + 1) \
                                                        / (count_prob_object["word_pos_count"].get(word, 0) + \
                                                            count_prob_object["word_neg_count"].get(word, 0) + \
                                                            len(count_prob_object["unique_words"]))                                         

        print(count_prob_object["word_neg_prob"]["amazing"])
        print(count_prob_object["word_pos_prob"]["amazing"])

dh = DataHandler()  
movie_df = dh.read_and_clean_data()
training_set, validation_set = dh.create_train_validation_sets(movie_df)
print(len(training_set))
print(len(validation_set))
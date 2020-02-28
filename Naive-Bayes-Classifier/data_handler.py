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

        print(movie_training_df.head(50))
        return movie_training_df

    @staticmethod
    def shuffle_data():
        return
    
    
    @staticmethod
    def get_counts(movie_training_df):
        '''Gets output counts + probability, word counts, union'''

        count_prob_object = {
            "neg_prob": 0,
            "pos_prob": 0,
            "unique_words": set(),
            "word_neg_counts": {},
            "word_pos_counts": {}
        }

        sentiment_count = movie_training_df.groupby("Sentiment").size()
        count_prob_object["neg_prob"] = sentiment_count["N"]/len(movie_training_df)
        count_prob_object["pos_prob"] = sentiment_count["P"]/len(movie_training_df)

        sentence_list = movie_training_df["Phrase"].str.split(" ")

        for sentence in sentence_list:
            for phrase in sentence:
                count_prob_object["unique_words"].add(phrase)
                
        return

'''
        phrase_list = movie_training_df["Phrase"].to_list()
        for phrase in phrase_list:
            print(phrase)
            for word in phrase.split(" "):
                if not word in count_prob_object["unique_words"]:
                    count_prob_object["unique_words"].append(word)
        
        print(count_prob_object["unique_words"])

'''
        

dh = DataHandler()  
movie_df = dh.read_and_clean_data()
dh.get_counts(movie_df)
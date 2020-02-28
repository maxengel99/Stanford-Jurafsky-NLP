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
        print(movie_training_df.head(10))
    
    @staticmethod
    def shuffle_data():
        return
    
    
    @staticmethod
    def get_counts():
        '''Gets output counts + probability, word counts, union'''
        
        return

dh = DataHandler()  
dh.read_and_clean_data()
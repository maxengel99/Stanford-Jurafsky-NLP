from data_handler import DataHandler as dh
from naive_bayes import NaiveBayes as nb

initial_training_data = dh.read_and_clean_data()
training_set, validation_set = dh.create_train_validation_sets(initial_training_data)
movie_data_info = dh.get_counts(training_set)

correct = 0

for _, row in validation_set.iterrows():
    total_neg_prob = nb.get_pred(row["Phrase"], movie_data_info, "N")
    total_pos_prob = nb.get_pred(row["Phrase"], movie_data_info, "P")

    pred = "N" if total_neg_prob > total_pos_prob else "P"

    if row["Sentiment"] == pred:
        correct += 1

print(correct/len(validation_set))
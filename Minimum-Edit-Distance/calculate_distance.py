import sys

def calculate_distance(original_word, transformed_word):
    # base case 1 - both strings blank
    if(len(original_word) == 0 and len(transformed_word) == 0):
        return 0, ''

    # base case 2 - only insertions left
    if(len(original_word) == 0):
        return len(transformed_word), 'i'*len(transformed_word)

    # base case 3 - only deletions left
    if(len(transformed_word) == 0):
        return len(original_word), 'd'*len(original_word)

    # same last character - cut off last letter
    if(original_word[-1] == transformed_word[-1]):
        no_change_info = list(calculate_distance(original_word[:-1], transformed_word[:-1]))
        return no_change_info[0], no_change_info[1] + 'n'

    # min between insertion and deletion
    insertion_info = list(calculate_distance(original_word[:-1], transformed_word))
    deletion_info = list(calculate_distance(original_word, transformed_word[:-1]))
    tmp_original_word = original_word
    tmp_original_word = tmp_original_word[:-1] + transformed_word[-1]
    replacement_info = list(calculate_distance(tmp_original_word[:-1], transformed_word[:-1]))

    if(replacement_info <= insertion_info and replacement_info <= deletion_info):
        return 1 + replacement_info[0], replacement_info[1] + 'r'
    elif(insertion_info <= deletion_info):
        return 1 + insertion_info[0], insertion_info[1] + 'd'
    else:
        return 1 + deletion_info[0], deletion_info[1] + 'i'

original_word = sys.argv[1]
transformed_word = sys.argv[2]

print(calculate_distance(original_word, transformed_word))
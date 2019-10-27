import sys

def calculate_distance(original_word, transformed_word):
    # base case 1 - both strings blank
    if(len(original_word) == 0 and len(transformed_word) == 0):
        return 0

    # base case 2 - only insertions left
    if(len(original_word) == 0):
        return len(transformed_word)

    # base case 3 - only deletions left
    if(len(transformed_word) == 0):
        return len(original_word)

    # same last character - cut off last letter
    if(original_word[-1] == transformed_word[-1]):
        return calculate_distance(original_word[:-1], transformed_word[:-1])

    # min between insertion and deletion
    insertion_info = 1 + calculate_distance(original_word[:-1], transformed_word)
    deletion_info = 1 + calculate_distance(original_word, transformed_word[:-1])

    tmp_original_word = original_word
    tmp_original_word = tmp_original_word[:-1] + transformed_word[-1]
    replacement_info = 1 + calculate_distance(tmp_original_word[:-1], transformed_word[:-1])

    if(replacement_info <= insertion_info and replacement_info <= deletion_info):
        return replacement_info
    elif(insertion_info <= deletion_info):
        return insertion_info
    else:
        return deletion_info

original_word = sys.argv[1]
transformed_word = sys.argv[2]

print(calculate_distance(original_word, transformed_word))
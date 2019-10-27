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
    if(original_word[len(original_word) - 1] == transformed_word[len(transformed_word) - 1]):
        return calculate_distance(original_word[:len(original_word) - 1], transformed_word[:len(transformed_word) - 1])

    # min between insertion and deletion
    return min(1 + calculate_distance(original_word[:len(original_word) - 1], transformed_word),
               1 + calculate_distance(original_word, transformed_word[:len(transformed_word) - 1]))

original_word = sys.argv[1]
transformed_word = sys.argv[2]

print(calculate_distance(original_word, transformed_word))
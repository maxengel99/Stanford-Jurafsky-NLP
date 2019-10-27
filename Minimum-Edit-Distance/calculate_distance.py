import sys

class AlignmentPoint:
    def __init__(self, original_letter, transformed_letter, alignment):
        self.original_letter = original_letter
        self.transformed_letter = transformed_letter
        self.alignment = alignment

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

cost_and_alignment_info = list(calculate_distance(original_word, transformed_word))
alignment_list = []

original_word_index = 0
transformed_word_index = 0

for alignment in cost_and_alignment_info[1]:
    if(alignment == 'n' or alignment == 'r'):
        alignment_list.append(AlignmentPoint(original_word[original_word_index], transformed_word[transformed_word_index], alignment))
        original_word_index += 1
        transformed_word_index += 1
    elif(alignment == 'd'):
        alignment_list.append(AlignmentPoint(original_word[original_word_index], '*', alignment))
        original_word_index += 1
    else:
        alignment_list.append(AlignmentPoint('*', transformed_word[transformed_word_index], alignment))
        transformed_word_index += 1

for item in alignment_list:
    print("Original letter - ", item.original_letter)
    print("Transformed letter - ", item.transformed_letter)
    print("Alignment - " + item.alignment)
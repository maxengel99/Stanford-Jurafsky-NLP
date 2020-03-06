## N-gram
## predict occurence of word based on its n-1 words
## Steps
## Get text
## read through text
## make calculations?

## word --> key that maps to list
## word --> key that maps to object
## object contains
## 1. total number of occurences
## 2. map of following word + # of occurances

from WordEntry import WordEntry

wordEntriesMap = {}

file = open("test.txt")
for sentence in file:
    word_list = sentence.split()
    for index, word in enumerate(word_list):
        if(index == 0):
            if '<s>' in wordEntriesMap:
                wordEntriesMap['<s>'].addWord(word)
            else:
                wordEntriesMap['<s>'] = WordEntry('<s>')
            continue

        if word in wordEntriesMap:
            wordEntriesMap[word].addWord(word_list[index + 1])
        else:
            wordEntriesMap[word] = WordEntry(word)
            wordEntriesMap[word].addWord(word_list[index + 1])

        
        if word in wordEntriesMap:
            wordEntriesMap[word_list[index - 1]].addWord(word)
        else:
            wordEntriesMap[word_list[index - 1]] = WordEntry()
        wordEntriesMap[word].addWord(word_list[index - 1])

        if(index == len(word_list) - 1):
            wordEntriesMap[word].addWord('</s>')
            continue

print(wordEntriesMap)
class WordEntry:
    def __init__(self, word):
        self.word = word
        self.count = 1
        self.followingWords = {}
    
    def addWord(self, followingWord):
        if followingWord in self.followingWords:
            self.followingWords[followingWord] += 1
        else:
            self.followingWords[followingWord] = 1
    
    def printList(self):
        for key in self.followingWords:
            print("{} contains {}".format(key, self.followingWords[key]))
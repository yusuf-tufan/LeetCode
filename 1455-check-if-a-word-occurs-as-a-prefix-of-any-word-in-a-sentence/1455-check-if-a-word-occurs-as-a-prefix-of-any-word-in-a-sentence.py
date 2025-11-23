class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        sentence=sentence.split()
        for i,words in enumerate(sentence):
            if words.startswith(searchWord):
                return i+1
        return -1
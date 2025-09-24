class Solution(object):
    def checkIfPangram(self, sentence):
        letters = "abcdefghijklmnopqrstuvwxyz"
        sentence=''.join(set(sentence))
        if len(letters)==len(sentence):
            return True
        else:
            return False
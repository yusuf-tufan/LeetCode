class Solution(object):
    def detectCapitalUse(self, word):
        up_word=word.upper()
        low_word=word.lower()

        capital_word=word[0].upper()
        word2=word.lower()
        word3=capital_word+word2[1:]
        

        if word==up_word:
            return True
        if word == low_word:
            return True
        if word == word3:
            return True
        else:
            return False


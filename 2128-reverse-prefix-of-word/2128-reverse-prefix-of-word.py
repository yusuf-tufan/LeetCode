class Solution(object):
    def reversePrefix(self, word, ch):
        if ch in word:
            c=word.index(ch)
            s=word[:c+1]
            word=word.replace(s,' ')
            s=s[::-1]
            new_word=word.replace(' ',s)
            return new_word
        return word
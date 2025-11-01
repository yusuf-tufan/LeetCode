class Solution(object):
    def sortSentence(self, s):
        s=s[::-1].split()
        s.sort()
        new_word=""
        for i in range(len(s)):
            s[i]=' '+s[i][1:]
            if s[i][1:].isalpha():
                new_word+=s[i][::-1]
        return new_word.strip()
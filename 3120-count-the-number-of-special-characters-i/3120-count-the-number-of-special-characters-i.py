class Solution(object):
    def numberOfSpecialChars(self, word):
        chars=[]
        for i in word:
            for x in word:
                if i.islower() and i.upper()==x:
                    if [i,x] not in chars:
                        chars.append([i,x])
        return len(chars)
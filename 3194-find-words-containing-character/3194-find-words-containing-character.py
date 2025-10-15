class Solution(object):
    def findWordsContaining(self, words, x):
        new_list=[]
        for i in range(0,len(words)):
            if x in words[i]:
                new_list.append(i)
        return new_list
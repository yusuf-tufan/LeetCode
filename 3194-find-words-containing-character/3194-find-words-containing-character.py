class Solution(object):
    def findWordsContaining(self, words, x):
        new_list=[]
        for i in range(0,len(words)):
            if x in words[i]:
                new_list.append(i)
        new_list=list(set(new_list))
        return (new_list)
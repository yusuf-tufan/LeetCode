class Solution(object):
    def countWords(self, words1, words2):
        clean_list=[]
        clean_list2=[]
        k=0
        for i in words1:
            if words1.count(i)==1:
                clean_list.append(i)
        for e in words2:
            if words2.count(e)==1:
                clean_list2.append(e)
        for c in clean_list:
            if c in clean_list2:
                k+=1
        return k
class Solution(object):
    def truncateSentence(self, s, k):
        s=s.split()
        new_list=[]
        for i in range(0,k):
            new_list.append(s[i])
        s=" ".join(new_list)
        return s
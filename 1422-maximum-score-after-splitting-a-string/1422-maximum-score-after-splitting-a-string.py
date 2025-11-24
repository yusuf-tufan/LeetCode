class Solution(object):
    def maxScore(self, s):
        sum_list=[]
        for i in range(len(s)-1):
            sum_list.append(s[:i+1].count('0')+s[i+1:].count('1'))
        return  max(sum_list)
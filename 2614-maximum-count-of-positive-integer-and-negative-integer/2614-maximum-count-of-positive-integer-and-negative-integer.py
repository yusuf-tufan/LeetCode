class Solution(object):
    def maximumCount(self, nums):
            positive=0
            negative=0
            for i in nums:
                if i<0:
                    negative+=1
                if i>0:
                    positive+=1
                else:
                    continue
            if positive<negative:
                return negative
            return positive
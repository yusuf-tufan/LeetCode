class Solution(object):
    def maximumCount(self, nums):
            pos=0
            neg=0
            for i in nums:
                if i<0:
                    neg+=1
                if i>0:
                    pos+=1
            if pos<neg:
                return neg
            return pos
class Solution(object):
    def sumBase(self, n, k):
        nums=[]
        count=0
        while n>0:
            remainder=n%k
            nums.append(remainder)
            n=n//k
        return sum(nums)
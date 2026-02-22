class Solution(object):
    def minOperations(self, nums, k):
        count=0
        sumNums=sum(nums)
        while sumNums % k!=0:
            sumNums-=1
            count+=1
        return count
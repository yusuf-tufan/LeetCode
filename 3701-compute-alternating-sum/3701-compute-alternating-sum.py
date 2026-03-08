class Solution(object):
    def alternatingSum(self, nums):
        sumNums=0
        for i in range(len(nums)):
            if i%2==0:
                sumNums+=nums[i]
            else:
                sumNums-=nums[i]
        return sumNums
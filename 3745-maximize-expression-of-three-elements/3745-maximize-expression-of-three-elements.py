class Solution(object):
    def maximizeExpressionOfThree(self, nums):
        a=max(nums)
        nums.remove(a)
        return a+max(nums)-min(nums)
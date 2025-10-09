class Solution(object):
    def missingNumber(self, nums):
        nums2=list(range(0,len(nums)+1))
        x=list(set(nums2)-set(nums))
        return x[0]
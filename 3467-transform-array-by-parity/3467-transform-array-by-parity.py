class Solution(object):
    def transformArray(self, nums):
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=nums[i]-nums[i]
            else:
                nums[i]=nums[i]-nums[i]+1
        return sorted(nums)
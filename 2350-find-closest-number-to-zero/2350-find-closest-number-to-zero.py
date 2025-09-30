class Solution(object):
    def findClosestNumber(self, nums):
        nums.append(0)
        nums.sort()
        if nums[-1]!=0:
            if abs(nums[nums.index(0)-1]) < nums[nums.index(0)+1]:
                return (nums[nums.index(0)-1])
            return nums[nums.index(0)+1]
        return nums[nums.index(0)-1]
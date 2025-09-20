class Solution(object):
    def findFinalValue(self, nums, original):
        if original in nums:
            for i in range(len(nums)):
                original=original*2
                if original not in nums:
                    return original      
        else:
            return original
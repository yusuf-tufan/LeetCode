class Solution(object):
    def findMissingElements(self, nums):
        return [i for i in range(min(nums),max(nums)+1) if i not in nums]
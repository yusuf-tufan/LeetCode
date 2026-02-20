class Solution(object):
    def minMoves(self, nums):
        nums.sort()
        bigNum=nums[-1]
        count=0
        for i in nums[0:-1]:
            count+=bigNum-i
        return count
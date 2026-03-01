class Solution(object):
    def minimumOperations(self, nums):
        count=0
        for i in nums:
            if i%3==2 or i%3==1:
                count+=1
        return count
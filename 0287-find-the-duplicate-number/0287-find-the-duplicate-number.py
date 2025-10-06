class Solution(object):
    def findDuplicate(self, nums):
        num_seen=set()
        for i in nums:
            if i in num_seen:
                return i
            num_seen.add(i)
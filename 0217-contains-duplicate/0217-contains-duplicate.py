class Solution(object):
    def containsDuplicate(self, nums):
        num_seen=set()
        for i in nums:
            if i in num_seen:
                return True
            num_seen.add(i)
        return False
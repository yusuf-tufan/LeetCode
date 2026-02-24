class Solution(object):
    def sumDivisibleByK(self, nums, k):
        groups={}
        result=0
        for num in nums:
            if num not in groups:
                groups[num]=[]
            groups[num].append(num)
        lists=groups.values()
        for i in lists:
            if len(i)%k==0:
                result+=sum(i)
        return result
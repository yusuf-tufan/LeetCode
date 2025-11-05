class Solution(object):
    def maxKDistinct(self, nums, k):
        nums=list(set(nums))
        nums.sort()
        new_list=[]
        if len(nums)<=k:
            return nums[::-1]
        for i in nums[::-1]:
            new_list.append(i)
            if len(new_list)==k:
                return new_list
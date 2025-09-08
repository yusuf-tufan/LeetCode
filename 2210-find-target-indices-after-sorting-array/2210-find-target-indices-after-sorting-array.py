class Solution(object):
    def targetIndices(self, nums, target):
        new_list=[]
        search=target
        nums.sort()
        for i,x in enumerate(nums):
            if x==target:
                new_list.append(i)
        return new_list
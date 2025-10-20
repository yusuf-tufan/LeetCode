class Solution(object):
    def thirdMax(self, nums):
        set_nums=sorted(set(nums),reverse=True)
        if len(set_nums)<3:
            return set_nums[0]
        else:
            return set_nums[2]
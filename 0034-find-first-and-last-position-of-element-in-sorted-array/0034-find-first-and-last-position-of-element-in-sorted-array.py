class Solution(object):
    def searchRange(self, nums, target):
        new_list=[]
        if target not in nums:
            return -1,-1

        for i,value in enumerate(nums):
            if value == target:
                new_list.append(i)
        if len(new_list)<=1:
            return nums.index(target),nums.index(target)
        else:
            return new_list[0],new_list[-1]

result = Solution()
result.searchRange([1,2,3,3,3,3,4,5,9],3)

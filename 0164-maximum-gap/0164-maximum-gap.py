class Solution(object):
    def maximumGap(self, nums):
        nums.sort()
        new_list=[]
        if len(nums)>=2:
            for i in range(0,len(nums)-1):
                new_list.append(abs(nums[i]-nums[i+1]))
            return max(set(new_list))
        return 0
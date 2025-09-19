class Solution(object):
    def findDisappearedNumbers(self, nums):
        num_set=set(nums)
        new_list=[]
        for i in range(1,len(nums)+1):
            if i not in num_set:
                new_list.append(i)
        return new_list
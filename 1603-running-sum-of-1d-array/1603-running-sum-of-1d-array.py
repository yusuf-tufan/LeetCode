class Solution(object):
    def runningSum(self, nums):
        count=0
        new_list=[]
        for i in nums:
            count+=i
            new_list.append(count)
        return new_list

class Solution(object):
    def findGCD(self, nums):
        max1=max(nums)
        min1=min(nums)
        new_list=[]
        for i in range(1,max1+1):
            if max1%i==0 and min1%i==0:
                new_list.append(i)
        return max(new_list)
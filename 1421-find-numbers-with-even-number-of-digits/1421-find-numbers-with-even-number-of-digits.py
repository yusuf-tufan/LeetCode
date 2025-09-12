class Solution(object):
    def findNumbers(self, nums):
        new_list=[]
        for i in nums:
            i=str(i)
            if len(i)%2==0:
                i=int(i)
                new_list.append(i)
        return len(new_list)
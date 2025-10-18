class Solution(object):
    def minElement(self, nums):
        sum_list=[]
        for i in nums:
            i=str(i)
            k=0
            for c in i:
                k+=int(c)
            sum_list.append(k)
        return min(sum_list)
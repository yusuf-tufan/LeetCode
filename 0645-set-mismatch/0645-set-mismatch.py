class Solution(object):
    def findErrorNums(self, nums):
        count=[0 for i in range(len(nums)+1)]
        for i in nums:
            count[i]+=1
        duplicate=0
        missing=0
        for x in range(1,len(nums)+1):
            if count[x]==2:
                duplicate=x
            if count[x]==0:
                missing=x
        return [duplicate,missing]
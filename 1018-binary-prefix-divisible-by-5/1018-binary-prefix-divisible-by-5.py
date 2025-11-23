class Solution(object):
    def prefixesDivBy5(self, nums):
        num=0
        boolean_list=[]
        for i in nums:
            num=(num*2+i)
            if num%5==0:
                boolean_list.append(True)
            else:
                boolean_list.append(False)
        return boolean_list
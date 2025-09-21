class Solution(object):
    def arraySign(self, nums):
        multiply=1
        for i in nums:
            multiply*=i
        if multiply<0:
            return -1
        else:
            if multiply==0:
                return 0
            return 1
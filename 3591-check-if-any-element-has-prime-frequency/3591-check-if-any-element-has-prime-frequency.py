class Solution(object):
    def checkPrimeFrequency(self, nums):
        for i in nums:
            freq=nums.count(i)
            count=1
            isprime=2
            while count<=freq:
                if  freq%count==0:
                    isprime-=1
                count+=1
            if isprime==0:
                return True
        return False
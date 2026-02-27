class Solution(object):
    def smallestAbsent(self, nums):
        average=int(sum(nums)/len(nums))
        num=average
        while True:
            if num>average and num not in nums and num>0:
                break
            num+=1
        return num
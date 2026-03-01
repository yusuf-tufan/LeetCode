class Solution(object):
    def getSneakyNumbers(self, nums):
        twoNums=[]
        for i in nums:
            if nums.count(i)==2:
                if i in twoNums:
                    continue
                twoNums.append(i)
        return twoNums
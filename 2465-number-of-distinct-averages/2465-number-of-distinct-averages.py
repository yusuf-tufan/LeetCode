class Solution(object):
    def distinctAverages(self, nums):
        listAverage=[]
        count=0
        while len(nums)!=0:
            minNums=min(nums)
            maxNums=max(nums)
            average=((minNums+maxNums)/2)
            nums.remove(minNums)
            nums.remove(maxNums)
            if average not in listAverage:
                listAverage.append(average)
                count+=1
        return count
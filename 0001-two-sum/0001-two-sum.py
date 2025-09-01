class Solution(object):
    def twoSum(self, nums, target):

        indexs=[]
        if len(nums)==2:
            return [0,1]
        else:
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if nums[i]+nums[j]==target:
                        indexs.append(i)
                        indexs.append(j)
            return indexs
result = Solution()
result.twoSum([3,2,3],6)
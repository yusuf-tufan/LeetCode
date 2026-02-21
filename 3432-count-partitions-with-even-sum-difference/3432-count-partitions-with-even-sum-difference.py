class Solution(object):
    def countPartitions(self, nums):
        forks=0
        count=0
        end=0
        for i in nums:
            if end==len(nums)-1:
                break
            forks+=i
            k=sum(nums)-count
            if (count-k)%2==0:
                count+=1
            end+=1
        return count
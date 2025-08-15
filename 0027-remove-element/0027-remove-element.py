class Solution(object):
    def removeElement(self, nums, val):
        while True:
            if val in nums:
                nums.remove(val)
            else:
                break
        print(nums)
s = Solution()
s.removeElement([3,2,2,3],2)

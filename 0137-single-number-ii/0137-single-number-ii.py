class Solution(object):
    def singleNumber(self, nums):
        new_nums=set()
        nums_num=set()
        for i in nums:
            if i in new_nums:
                nums_num.add(i)
            new_nums.add(i)
        for c in nums_num:
            new_nums.remove(c)
        new_nums=list(set(new_nums))
        return new_nums[0]
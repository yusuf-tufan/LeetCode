class Solution(object):
    def pivotArray(self, nums, pivot):
        low_array=list()
        equal_array=list()
        big_array=list()
        for i in nums:
            if i<pivot:
                low_array.append(i)
            elif i==pivot:
                equal_array.append(i)
            else:
                big_array.append(i)
        return low_array+equal_array+big_array
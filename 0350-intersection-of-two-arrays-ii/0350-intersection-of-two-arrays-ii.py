class Solution(object):
    def intersect(self, nums1, nums2):
        same_chars=[]
        copy_num2=nums2.copy()
        for i in nums1:
            if i in copy_num2:
                same_chars.append(i)
                copy_num2.remove(i)
        return same_chars
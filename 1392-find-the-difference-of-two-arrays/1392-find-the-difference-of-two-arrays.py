class Solution(object):
    def findDifference(self, nums1, nums2):
        answer0=[]
        answer1=[]
        for i in nums1:
            if i not in nums2:
                answer0.append(i)
        for x in nums2:
            if x not in nums1:
                answer1.append(x)
        answer0=list(set(answer0))
        answer1=list(set(answer1))
        new_list=[answer0,answer1]
        return new_list

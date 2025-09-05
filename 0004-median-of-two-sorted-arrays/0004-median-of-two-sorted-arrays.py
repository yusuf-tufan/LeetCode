class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        new_list=[]
        t=[]
        new_list.extend(nums1)
        new_list.extend(nums2)
        new_list.sort()
        a = len(new_list) // 2
        c = new_list[a]
        if len(new_list)%2!=0:
            return c
        else:
            e=new_list[a-1]
            t.append(c)
            t.append(e)
            r=sum(t)/2
            if r<0:
                return 0
            return r
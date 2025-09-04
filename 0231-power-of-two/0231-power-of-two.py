class Solution(object):
    def isPowerOfTwo(self, n):
        new_list=[]
        for c in range(0,40):
            k=2**c
            new_list.append(k)
        if n in new_list:
            return True
        else:
            return False
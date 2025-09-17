class Solution(object):
    def kthFactor(self, n, k):
        new_list=[]
        for i in range(1,n+1):
            if n%i==0:
                new_list.append(i)
        if len(new_list)<k:
            return -1
        return new_list[k-1]

        
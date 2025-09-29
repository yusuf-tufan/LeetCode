class Solution(object):
    def subtractProductAndSum(self, n):
        k=1
        l=0
        n=str(n)
        for i in n:
            k*=int(i)
            l+=int(i)
        return k-l
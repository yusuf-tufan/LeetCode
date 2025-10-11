class Solution(object):
    def isPowerOfThree(self, n):
        c=3
        k=-3
        if n==-3:
            return False
        for i in range(20):
            c*=3
            if i%2!=0:
                k**i
            if c==n or k==n or n==1 or n==3:
                return True
                break
        return False
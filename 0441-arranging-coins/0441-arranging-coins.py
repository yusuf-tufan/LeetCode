class Solution(object):
    def arrangeCoins(self, n):
        k=int((-1+(1+8*n)**(1/2))//2)
        return k
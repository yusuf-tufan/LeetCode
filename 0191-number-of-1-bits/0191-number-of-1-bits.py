class Solution(object):
    def hammingWeight(self, n):
        k=sum([int(i) for i in bin(n)[2:]])
        return k
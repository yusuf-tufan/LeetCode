class Solution(object):
    def minimumFlips(self, n):
        newN=bin(n)[2:]
        count=0
        for i,j in zip(newN,newN[::-1]):
            if i!=j:
                count+=1
        return count 
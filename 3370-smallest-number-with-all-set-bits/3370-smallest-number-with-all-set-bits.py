class Solution(object):
    def smallestNumber(self, n):
        while True:
            binN=bin(n)[2:]
            if '0' not in binN:
                return n
            n+=1

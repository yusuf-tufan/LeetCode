class Solution(object):
    def mirrorDistance(self, n):
        newN=str(n)[::-1]
        return abs(n-int(newN))

        
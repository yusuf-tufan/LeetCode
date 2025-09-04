class Solution(object):
    def findClosest(self, x, y, z):
        a=abs(z-x)
        b=abs(z-y)
        if a<b:
            return 1
        else:
            if a==b:
                return 0
            return 2
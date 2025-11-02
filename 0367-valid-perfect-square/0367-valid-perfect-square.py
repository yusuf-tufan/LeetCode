class Solution(object):
    def isPerfectSquare(self, num):
        c=num**(1/2)
        if c==int(c):
            return True
        return False
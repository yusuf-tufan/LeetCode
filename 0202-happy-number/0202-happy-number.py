class Solution(object):
    def isHappy(self, n):   
        seen = set()
        while n!=1:
            if n in seen:
                return False
            seen.add(n)
            newN=0
            while n>0:
                digit=n%10
                newN+=digit*digit
                n=n//10 
            n = newN
        return True

class Solution(object):
    def isAnagram(self, s, t):
        s=list(s)
        t=list(t)
        s.sort()
        t.sort()
        if s==t:
            return True
        return False
class Solution(object):
    def findPermutationDifference(self, s, t):
        result=0
        for i in s:
            for x in t:
                if i==x:
                    result+=abs(s.index(i)-t.index(x))
        return result
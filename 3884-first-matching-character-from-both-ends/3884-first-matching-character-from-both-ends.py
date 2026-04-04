class Solution(object):
    def firstMatchingIndex(self, s):
        result=101
        for i in range(0,len(s)):
            if s[i]==s[len(s)-i-1]:
                if i<result:
                    result=i
        if result==101:
            return -1
        return result
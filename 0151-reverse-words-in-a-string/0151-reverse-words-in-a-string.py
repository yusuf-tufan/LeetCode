class Solution(object):
    def reverseWords(self, s):
        s=s.split()
        a= ' '.join(s[::-1])
        return a
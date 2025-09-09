class Solution(object):
    def reverseWords(self, s):
        reverse_s=s[::-1].split()
        word=' '.join(reverse_s[::-1])
        return word

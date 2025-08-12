class Solution:
    def isPalindrome(self, x: int):
        a=str(x)
        rewievnum=a[::-1]
        status=True
        if (a!= rewievnum):
            status=False
        return status
status=True
s=Solution()
s.isPalindrome(121)
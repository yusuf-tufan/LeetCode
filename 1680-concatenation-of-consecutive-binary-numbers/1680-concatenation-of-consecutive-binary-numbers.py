class Solution(object):
    def concatenatedBinary(self, n):
        count=1
        strBin=""
        while count<=n:
            strBin+=str(bin(count)[2:])
            count+=1
        return int(strBin,2)%(10**9+7)
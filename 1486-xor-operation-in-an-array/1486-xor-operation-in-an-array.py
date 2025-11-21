class Solution(object):
    def xorOperation(self, n, start):
        xor_result=0
        for i in range(0,n):
            xor_result^=start + 2 * i
        return xor_result
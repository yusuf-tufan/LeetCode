class Solution(object):
    def bitwiseComplement(self, n):
        n=bin(n)[2:]
        k=''
        for i in n:
            if i=='1':
                i='0'
                k+=i
            else:
                i='1'
                k+=i
        return int(k,2)
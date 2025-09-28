class Solution(object):
    def reverseBits(self, n):
        new_n=format(n,'032b')
        new_n=new_n[::-1]
        new_num=int(new_n,2)
        return new_num
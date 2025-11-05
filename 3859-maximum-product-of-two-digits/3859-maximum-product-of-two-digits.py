class Solution(object):
    def maxProduct(self, n):
        multiply_num=1
        if len(str(n))==2:
            for i in str(n):
                multiply_num*=int(i)
            return multiply_num
        else:
            n=str(n)
            n=sorted(n)
            multiply_num2=int(n[-2:][0]) * int(n[-2:][1])
            return multiply_num2
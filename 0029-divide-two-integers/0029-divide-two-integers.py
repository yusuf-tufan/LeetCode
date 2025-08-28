class Solution(object):
    def divide(self, dividend, divisor):
        if dividend==-2147483648 and divisor==-1:
            return 2147483647
        else:
            r=abs(dividend)/abs(divisor)
            r=str(r)
            r=r.split('.')
            r=int(r[0])
            if divisor<0 and dividend<0:
                return r
            else:
                if divisor<0 or dividend<0:
                    r = str(r)
                    r = '-' + r
                    return int(r)
                else:
                    return r
result = Solution()
result.divide(-1,-1)
class Solution(object):
    def reverse(self, x):
        if x==0:
            return 0
        x = str(x)
        if '-' in x[0]:
            x = x.replace('-', "")
            x=int('-'+x[::-1])
            if x<-2147483641:
                return 0
            return x
        else:
            if '0' in x[0]:
                x = x[0].replace('0', '')
                return int(x[::-1])
            else:
                if int(x[::-1])>=2147483651:
                    return 0
                else:
                    return int(x[::-1])
result = Solution()
result.reverse(154)

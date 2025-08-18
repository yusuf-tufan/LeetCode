import math
from math import sqrt
class Solution(object):
    def mySqrt(self, x):
        new_list=[]
        i = float(sqrt(x))
        new_list.append(i)
        return math.trunc(i)

result = Solution()
result.mySqrt(8)


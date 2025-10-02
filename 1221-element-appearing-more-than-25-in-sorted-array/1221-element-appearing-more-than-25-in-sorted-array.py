from collections import Counter
class Solution(object):
    def findSpecialInteger(self, arr):
        c=len(arr)/4
        f=Counter(arr)
        if f.most_common(1)[0][1] >c:
            return (f.most_common(1)[0][0])
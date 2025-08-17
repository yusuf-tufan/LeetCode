class Solution(object):
    def plusOne(self, digits):
        newlist=[]
        i=int(''.join(map(str,digits)))+1
        i=str(i)
        for a in i :
            a=int(a)
            newlist.append(a)
        return newlist
result = Solution()
result.plusOne([1,2,3])

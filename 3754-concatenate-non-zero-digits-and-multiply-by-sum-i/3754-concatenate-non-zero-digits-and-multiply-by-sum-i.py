class Solution(object):
    def sumAndMultiply(self, n):
        n=str(n)
        sumNums=0
        numsNoZero=''
        for i in n:
            if i!='0':
                sumNums+=int(i)
                numsNoZero+=i
        if len(numsNoZero)==0:
            return 0
        return int(numsNoZero)*sumNums
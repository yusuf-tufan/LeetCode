class Solution(object):
    def isThree(self, n):
        count=0
        for i in range(1,n+1):
            if n%i==0:
                count+=1
            else:
                continue
        if count==3:
            return True
        return False
        
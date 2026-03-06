class Solution(object):
    def canAliceWin(self, n):
        if n<10:
            return False
        else:
            s=0
            n=n-10
            count = 9
            if n<count:
                return True
            while n>0:
                n=n-count
                if n<0:
                    break
                count-=1
                s+=1
            if s%2==0:
                return True
            return False
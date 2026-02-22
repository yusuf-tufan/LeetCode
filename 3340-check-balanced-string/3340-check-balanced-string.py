class Solution(object):
    def isBalanced(self, num):
        sumOddIndx=0
        sumCoupleIndx=0
        for i in range(len(num)):
            if i%2==0:
                sumCoupleIndx+=int(num[i])
            else:
                sumOddIndx+=int(num[i])
        if sumOddIndx!=sumCoupleIndx:
            return False
        return True
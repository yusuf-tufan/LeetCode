class Solution(object):
    def numberOfSteps(self, num):
        count=0
        if num>0:
            while True:
                if num%2==0:
                    num=num//2
                else:
                    num=num-1
                count += 1
                if num ==0:
                    return count
        else:
            return 0
class Solution(object):
    def smallestNumber(self, n, t):
        sumNum=1
        while True:
            for i in str(n):
                sumNum*=int(i)
            if sumNum%t==0:
                return n
            n+=1
            sumNum=1
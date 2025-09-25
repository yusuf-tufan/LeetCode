class Solution(object):
    def sumOfMultiples(self, n):
        sum_nums=0
        for i in range(0,n+1):
            if i%3==0 or i%5==0 or i%7==0:
                sum_nums+=i
        return sum_nums
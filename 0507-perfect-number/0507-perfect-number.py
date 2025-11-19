class Solution(object):
    def checkPerfectNumber(self, num):
        if num<=1:
            return False
        sum_count=1
        i=2
        nums=int(num**0.5)
        while i<=nums:
            if num%i==0:
                sum_count+=i
                if i!=num//i:
                    sum_count+=num//i
            i+=1
        return sum_count==num
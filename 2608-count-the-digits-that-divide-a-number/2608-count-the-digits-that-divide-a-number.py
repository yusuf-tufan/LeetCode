class Solution(object):
    def countDigits(self, num):
        num_test=str(num)
        c=0
        for i in num_test:
            if num%int(i)==0:
                c+=1
        return c
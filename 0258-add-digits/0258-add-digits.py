class Solution(object):
    def addDigits(self, num):
        while True:
            c = 0
            num = str(num)
            for i in range(0,len(num)):
                c+=int(num[i])
            num=c
            if num<10:
                return num
                break
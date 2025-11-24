class Solution(object):
    def findComplement(self, num):
        num=bin(num)[2:]
        new_num=''
        for i in num:
            if i=='1':
                new_num+='0'
            else:
                new_num+='1'
        return int(new_num,2)
class Solution(object):
    def processStr(self, s):
        new_s=""
        for i in s:
            print(i)
            if i.isalpha():
                new_s+=i
            elif i=='*':
                new_s=new_s[:-1]
            elif i=='#':
                new_s+=new_s
            elif i=='%':
                new_s=new_s[::-1]
        return new_s
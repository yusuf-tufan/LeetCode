class Solution(object):
    def hasAlternatingBits(self, n):
        n=bin(n)[2:]
        n=str(n)
        new_list=[]
        for x in range(len(n)-1):
            if n[x]!=n[x+1]:
                continue
            else:
                new_list.append('False')
        if 'False' in set(new_list):
            return False
        return True
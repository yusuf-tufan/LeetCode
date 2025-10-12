class Solution(object):
    def countBits(self, n):
        sum_bit_list=[]
        for i in range(n+1):
            i=bin(i)
            c=0
            if '0b' in i:
                i=i.replace('0b','')
                if len(i)>1:
                    for x in i:
                        c+=int(x)
                    sum_bit_list.append(c)
                else:
                    sum_bit_list.append(int(i))
        return sum_bit_list
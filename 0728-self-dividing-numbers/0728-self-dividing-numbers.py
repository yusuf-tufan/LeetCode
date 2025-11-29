class Solution(object):
    def selfDividingNumbers(self, left, right):
        new_list=[]
        for i in range(left,right+1):
            count=0
            len_i=len(str(i))
            if '0' not in str(i):
                for x in str(i):
                    if i%int(x)==0:
                        count+=1
                    if len_i==count:
                        new_list.append(i)
        return new_list
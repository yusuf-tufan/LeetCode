class Solution(object):
    def tribonacci(self, n):
        t_list=[0,1,1]
        if n==2 or n==1:
            return 1
        elif n==0:
            return 0
        else:
            count=3
            while count<=n:
                t_list.append(t_list[count-1]+t_list[count-2]+t_list[count-3])
                count+=1
            return t_list[-1]
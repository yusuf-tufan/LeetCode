class Solution(object):
    def fib(self, n):
        new_list=[1,1]
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            for i in range(2,n):
                c=new_list[i-2]+new_list[i-1]
                new_list.append(c)
            return new_list[-1]
        
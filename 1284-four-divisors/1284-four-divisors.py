class Solution(object):
    def sumFourDivisors(self, nums):
        new_list=[]
        for i in nums:
            num_list=set()
            for x in range(1,int(i**0.5)+1):
                if i%x==0:
                    num_list.add(x)
                    num_list.add(i//x)
                    if len(new_list)>4:
                        break
            new_list.append(num_list)
        sum_list=[]
        for i in range(0,len(new_list)):
            if len(new_list[i])==4:
                sum_list.append(sum(new_list[i]))
        return sum(sum_list)
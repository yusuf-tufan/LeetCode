class Solution(object):
    def secondHighest(self, s):
        new_list=[]
        for i in s:
            if i.isdigit():
                new_list.append(i)
        new_list=list(set(new_list))
        if len(new_list)==0:
            return -1
        else:
            if len(new_list)==1:
                return -1
            else:
                new_list.sort()
                new_list.remove(new_list[-1])
                return int(new_list[-1])
class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr=sorted(arr)
        count_list=set()
        for i in range(len(arr)-1):
            count =arr[i + 1]-arr[i]
            count_list.add(count)
            if len(count_list)!=1:
                return False
        return True
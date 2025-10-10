class Solution(object):
    def heightChecker(self, heights):
        new_list=[i for i in heights]
        count=0
        heights.sort()
        for x in range(0,len(new_list)):
            if heights[x] !=new_list[x]:
                count+=1
        return count
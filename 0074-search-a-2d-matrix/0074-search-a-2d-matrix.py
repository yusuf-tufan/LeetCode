class Solution(object):
    def searchMatrix(self, matrix, target):
        new_list=[]
        for i in matrix:
            for c in i:
                new_list.append(c)
        if target in new_list:
            return True
        else:
            return False
result = Solution()
result.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],10)
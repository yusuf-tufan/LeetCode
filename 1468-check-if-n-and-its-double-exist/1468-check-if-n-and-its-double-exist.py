class Solution(object):
    def checkIfExist(self, arr):
        for i in range(0,len(arr)):
            for j in range(0,len(arr)):
                if i!=j and arr[i]==2*arr[j]:
                    return True
        return False        

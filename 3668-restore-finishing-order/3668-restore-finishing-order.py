class Solution(object):
    def recoverOrder(self, order, friends):
        resultList=[]
        for i in order:
            if i in friends:
                resultList.append(i)
        return (resultList)
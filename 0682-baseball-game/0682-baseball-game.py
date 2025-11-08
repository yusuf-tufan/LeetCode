class Solution(object):
    def calPoints(self, operations):
        opsList=[]
        for i in operations:
            if i=='D':
                opsList.append(opsList[-1]*2)
            elif i=='C':
                opsList.pop()
            elif i =='+':
                opsList.append(opsList[-2]+opsList[-1])
            else:
                opsList.append(int(i))
        return sum(opsList)
            
class Solution(object):
    def earliestTime(self, tasks):
        minTime=sum(tasks[0])
        for i in range(1,len(tasks)):
            sumTime=sum(tasks[i])
            if sumTime<minTime:
                minTime=sumTime
        return minTime
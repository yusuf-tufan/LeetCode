class Solution(object):
    def toggleLightBulbs(self, bulbs):
        onBulbsList=set()
        for i in bulbs:
            if i in onBulbsList:
                onBulbsList.remove(i)
            else:
                onBulbsList.add(i)
        return sorted(onBulbsList)
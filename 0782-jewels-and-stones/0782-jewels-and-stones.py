class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count=0
        for i in stones:
            for x in jewels:
                if x == i:
                    count+=1
        return count
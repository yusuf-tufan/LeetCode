class Solution(object):
    def hammingDistance(self, x, y):
        numx=f'{x:032b}'
        numy=f'{y:032b}'
        count=0
        for i,x in zip(numx,numy):
            if i!=x:
                count+=1
        return count
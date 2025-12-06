class Solution(object):
    def recoverOrder(self, order, friends):
        return [i for i in order if i in friends]
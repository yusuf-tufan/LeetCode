class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        result=100
        purchaseAmount=purchaseAmount/10
        return result-(int(purchaseAmount+0.5)*10)
        
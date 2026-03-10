class Solution(object):
    def getLeastFrequentDigit(self, n):
        listOfdigits=[]
        while n!=0:
            digit=n%10
            listOfdigits.append(digit)
            n=n//10
        listOfdigits.sort()
        countNum=10000
        resultDigit=0
        for i in listOfdigits:
            if listOfdigits.count(i)<countNum:
                countNum=listOfdigits.count(i)
                resultDigit=i
        return resultDigit
class Solution(object):
    def average(self, salary):
        salary.sort()
        salary.remove(salary[0])
        salary.remove(salary[-1])
        a=sum(salary)
        return a/len(salary)
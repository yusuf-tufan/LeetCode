class Solution(object):
    def convertDateToBinary(self, date):
        year_bin=bin(int(date[:4]))[2:]+'-'
        month=bin(int(date[5:7]))[2:]+'-'
        day=bin(int(date[8:10]))[2:]
        result=year_bin+month+day
        return result
class Solution(object):
    def dayOfYear(self, date):
        days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        february29=[1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948,
 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996,
 2000, 2004, 2008, 2012, 2016]
        if int(date[0]+date[1]+date[2]+date[3]) in february29 :
            days[1]=29
        x = date[5] + date[6]
        if '0' in date[5]:
            x = x.replace('0', '')
        k=0
        for i in range(int(x)-1):
            k+=days[i]
        r = date[8] + date[9]
        if '0' in date[8]:
            r = r.replace('0', '')
        return k+int(r)

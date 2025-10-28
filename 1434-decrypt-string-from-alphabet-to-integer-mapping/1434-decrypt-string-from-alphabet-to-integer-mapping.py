class Solution(object):
    def freqAlphabets(self, s):
        count=['j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        count2=['','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        for i in range(10,27):
            if str(i)+'#' in s:
               s=s.replace(str(i)+'#',count[i-10])
        for x in range(1,10):
            if str(x) in s:
                s=s.replace(str(x),count2[x])
        return s
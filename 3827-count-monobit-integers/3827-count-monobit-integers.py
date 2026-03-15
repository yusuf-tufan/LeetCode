class Solution(object):
    def countMonobit(self, n):
        count = 1
        for i in range(1, n+1):
            binN = bin(i)[2:]
            if binN.count('1') == len(binN):
                count += 1
        return count
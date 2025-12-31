class Solution(object):
    def longestCommonPrefix(self, strs):
        word1=strs[0]
        for i in strs[1:]:
            while not i.startswith(word1):
                word1=word1[:-1]
                if word1=="":
                    return ""
        return word1
class Solution(object):
    def strStr(self, haystack, needle):
        list1=[haystack]
        for i in list1:
            if needle in i:
                a=i.find(needle)
                list1.append(a)
                return list1[1]
                break
            else:
                return -1
result=Solution()
result.strStr("sadbutsad","sad")
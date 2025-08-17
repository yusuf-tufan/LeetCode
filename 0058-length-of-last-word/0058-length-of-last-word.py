class Solution(object):
    def lengthOfLastWord(self, s):
        new_list=[]
        words=(','.join(s.split()))
        new_list.append(words.split(','))
        return len(new_list[-1][-1])
result = Solution()
result.lengthOfLastWord("Hello World")

        
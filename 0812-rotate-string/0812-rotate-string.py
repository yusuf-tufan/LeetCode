class Solution(object):
    def rotateString(self, s, goal):
        new_list=[]
        if len(s)!=len(goal):
            return False
        for i in range(len(s)):
            word=s[i:]+s[:i]
            new_list.append(word)
        if goal in new_list:
            return True
        else:
            return False
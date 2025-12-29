class Solution(object):
    def shortestToChar(self, s, c):
        answers=[i for i in range(len(s))]
        prev=-len(s)
        for i in range(len(s)):
            if s[i]==c:
                prev=i
            answers[i]=i-prev
        prev=len(s)*2
        for x in range(len(s)-1,-1,-1):
            if s[x]==c:
                prev=x
            answers[x]=min(answers[x],prev-x)
        return answers
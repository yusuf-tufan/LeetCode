class Solution(object):
    def vowelConsonantScore(self, s):
        vowelsList=['a', 'e', 'i', 'o','u']
        consonants = [
    'b','c','d','f','g','h','j','k','l','m',
    'n','p','q','r','s','t','v','w','x','y','z'
]
        v=0
        c=0
        for i in s:
            if i in vowelsList:
                v+=1
            if i in consonants:
                c+=1
        if c>0:
            return v//c
        return 0
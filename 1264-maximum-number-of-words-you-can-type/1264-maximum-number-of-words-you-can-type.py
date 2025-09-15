class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        new_text=text.split()
        for c in range(len(new_text)):
            for i in brokenLetters:
                for x in new_text:
                    if i in x:
                        new_text.remove(x)
        return len(new_text)
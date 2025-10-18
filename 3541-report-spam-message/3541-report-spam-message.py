from collections import Counter
class Solution(object):
    def reportSpam(self, message, bannedWords):
        k=0
        message_counter=Counter(message)
        for i in set(bannedWords):
                k+=message_counter.get(i,0)
                if k>=2:
                    return True
        return False
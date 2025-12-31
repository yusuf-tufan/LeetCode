class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s)!=len(t):
            return False
        sTot={}
        tTos={}
        for chars_s,chars_t in zip(s,t):
            if chars_s in sTot and sTot[chars_s]!=chars_t:
                return False
            if chars_t in tTos and tTos[chars_t]!=chars_s:
                return False
            sTot[chars_s]=chars_t
            tTos[chars_t]=chars_s
        return True
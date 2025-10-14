class Solution(object):
    def findWords(self, words):
        top_row2 = set('qwertyuiop')
        middle_row2 = set('asdfghjkl')
        bottom_row2 = set('zxcvbnm')
        new_list=[]
        true_list=[]
        for i in words:
            new_list.append(i)
        for x in new_list:
            x2=x.lower()
            if set(x2).issubset(top_row2):
                true_list.append(x)
            elif set(x2).issubset(middle_row2):
                true_list.append(x)
            elif set(x2).issubset(bottom_row2):
                true_list.append(x)
        return true_list
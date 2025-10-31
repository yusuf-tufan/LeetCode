class Solution(object):
    def nextGreatestLetter(self, letters, target):
        letters=list(set(letters))
        if target not in letters:
            letters.append(target)
            letters=sorted(letters)
            target_indx=letters.index(target)
            if target_indx+1<len(letters):
                if target_indx+1<len(letters):
                    result=letters[target_indx+1]
                    return result
        else:
            letters=sorted(letters)
            target_indx2=letters.index(target)
            if target_indx2+1<len(letters):
                return letters[target_indx2+1]
        return letters[0]
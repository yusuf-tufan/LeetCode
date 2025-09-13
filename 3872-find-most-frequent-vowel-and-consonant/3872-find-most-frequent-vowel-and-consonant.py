class Solution(object):
    def maxFreqSum(self, s):
        vowels=[ 'a', 'e', 'i', 'o', 'u']
        new_vowels=[]
        consonants=[]
        new_vowels_num=0
        consonants_num=0
        for i in s:
            if i in vowels:
                new_vowels.append(i)
            else:
                consonants.append(i)
        if len(new_vowels)==0:
            new_vowels_num=0
        else:
            k = max(set(new_vowels), key=new_vowels.count)
            for x in new_vowels:
                if x == k:
                    new_vowels_num += 1
        if len(consonants)==0:
            consonants_num=0
        else:
            l = max(set(consonants), key=consonants.count)
            for y in consonants:
                if y==l: 
                    consonants_num+=1
        return new_vowels_num+consonants_num 
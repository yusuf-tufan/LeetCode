class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        lowercase_letters = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
        first_list = []
        second_list=[]
        target_list=[]
        num=''
        num2=''
        num3=''
        for i in firstWord:
            r=lowercase_letters.index(i)
            first_list.append(str(r))
            num=''.join(first_list)
            if num[0]=='0':
                num=num.replace(num[0],'',1)
        for x in secondWord:
            c=lowercase_letters.index(x)
            second_list.append(str(c))
            num2=''.join(second_list)
            if num2[0]=='0':
                num2=num2.replace(num2[0],'',1)
        for y in targetWord:
            z=lowercase_letters.index(y)
            target_list.append(str(z))
            num3=''.join(target_list)
            if num3[0]=='0':
                num3=num3.replace(num3[0],'',1)
        if len(num)==0:
            num=0
        if len(num2)==0:
            num2=0
        if len(num3)==0:
            num3=0
        num=int(num)
        num2=int(num2)
        num3=int(num3)
        summ_nums=num+num2
        if summ_nums==num3:
            return True
        else:
            return False
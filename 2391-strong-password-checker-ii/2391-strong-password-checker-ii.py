class Solution(object):
    def strongPasswordCheckerII(self, password):
        special_chars="!@#$%^&*()-+"
        has_digit = False
        has_upper = False
        has_lower = False
        has_special = False
        for z in range(0,len(password)-1):
            if password[z]==password[z+1]:
                return False
        for i in password:
            if i.isdigit():
                has_digit = True
            elif i.isupper():
                has_upper = True
            elif i.islower():
                has_lower=True
            elif i in special_chars:
                has_special=True
        if len(password)>7 and has_digit and has_lower and has_special and has_upper:
            return True
        else:
            return False
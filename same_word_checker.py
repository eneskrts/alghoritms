# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 14:03:14 2019

@author: Enes Karatas



Program claims check 2 strings is same or not.
calc function helps us to prevent exceptional issues like 'ragn' and 'angara'. They has same letters but not same all. ragn needs 2 'a' letter.If we didnt write calc function to check counts,program says they re same expression.

"""
def calc(character,str1,str2):
    a=str1.count(character)
    b=str2.count(character)
    
    return a==b
def check(str1,str2):
    for i in str1:
        if i in str2:
            if calc(i,str1,str2):
                pass
            else:
                return False
        elif i not in str2:
            return False
    return True
print(check("sena","enes"))

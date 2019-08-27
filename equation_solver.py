# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 14:41:38 2019

@author: Enes Karatas
"""
def isnumber(x):
    no="0123456789"
    return x in no

def spliting_numbers():
    pass

def find_missing_value(exp):
    x=exp.replace(" ","")
    sum='+'
    sub='-'
    multip='*'
    div='/'
    if sum in x:
        eq=x.split('=')
        print(eq[1]) #result number
        nums=eq[0].split('+')
        #print(nums) left side of equation
        digit=0
        uk_number=""
        print(nums)
#        digit=nums.index('x')
        for i in nums:
            if not 'x' in i:
                digit=int(i)
        if 'x' in nums[0]:
            uk_number=nums[0]
            digit=1
        else:
            uk_number=nums[1]
            
        n1=int(nums[digit])
        n2=int(eq[1])
        print(n2-n1)
        res1=str(n2-n1)
        
        t=uk_number.index('x')
        print(res1[t])
            
        
        
            

find_missing_value("1x+ 4=19")

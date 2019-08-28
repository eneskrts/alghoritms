# -*- coding: utf-8 -*-
"""
Code makes given list into 2 element cluster. Then search list to find a symmetric element. If not, output says which element doesnt have.

@author: Enes
"""
def arastr(arr):
#    print(type(arr[0]))
    for i in range(len(arr)):
        temp=arr[i]
#        print(type(temp))
    
        temp=temp[::-1]
#        print(temp)
        if temp in arr:
           pass
        else:
            return temp[::-1]
        
    
    
    
    
    
def parcala(arr):
    
   
    b=slice(2)
    new_l=[]

    for i in range(int(len(arr)/2)):
        new_l.append(list(arr[b]))
        del arr[:2]
    
    
    return new_l


            
            
a=[5,6,6,5,3,2]

z=parcala(a)


print(arastr(z))

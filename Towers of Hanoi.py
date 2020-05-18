# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:01:56 2020

@author: hemanth
"""
count = 0

def towers_of_hanoi(A, B, C,n):
    global count
    if n == 1:
        C.append(A.pop())
        count+=1
    else:
        towers_of_hanoi(A,C,B,n-1)
        towers_of_hanoi(A,B,C,1)
        towers_of_hanoi(B,A,C,n-1)
    return count

A = [i for i in range(14,0,-1)]
B = []
C = []

print(towers_of_hanoi(A,B,C,14))

print(C)

        
    
    


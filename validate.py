# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# This is a comment

def validate(string):
    
    values = {
        '(' : ')',
        '{' : '}',
        '[' : ']'        
        }
    
    if not string:
        return True
    
    stack = []
    
    for char in string:
        if char in values.keys():
            stack.append(char)
        else:
            if not stack:
                return False
            top = stack.pop()
            if char == values[top]:
                continue
            else: return False

    if not stack:
        return True
    return False

string1 = ')'
string2 = '[({)})]'

print(validate(string1))
#print(validate(string2))
            
    
                
        
        
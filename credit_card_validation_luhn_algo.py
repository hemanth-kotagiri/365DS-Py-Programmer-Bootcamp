# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:22:16 2020

@author: heman
"""

def isValid(numbers):
    length = len(str(numbers))
    """Checks if the given credit card number is valid"""
    not_multiplied = 0
    mul = 0
    # Step 1. Multiply all the 2nd digit by 2 from second to last.

    for i in range(1, len(str(numbers)), 2):
        current = sum(map(int, list(str(int(str(numbers)[i]) * 2))))
        mul += current
        not_multiplied += int(str(numbers)[i - 1])
    
    not_multiplied += int(str(numbers)[-1])

    return (mul + not_multiplied) % 10 == 0

print(isValid(371449635398431))
print(isValid(4166441502990250))

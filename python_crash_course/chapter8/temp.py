# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#def is_even_with_return(i):
#    """
#    Input: i, a positive int
#    Returns: True if i is even, otherwise False
#    """
#    print("with return")
#    reminder = i % 2
#    return reminder == 0
#
#is_even_with_return(3)
#print(is_even_with_return(3))
#
#def is_even_without_return(i):
#    """
#    Input: i, a positive int
#    Return: Does not return anything
#    """
#    print("without return")
#    remainder = i % 2
#    
#is_even_without_return(3)
#print(is_even_without_return(3))
#
#print(type(is_even_without_return(3)))

def is_even(i):
    """
    Input: i, a positive int
    Return: True if i is even, otherwise False
    """
    remainder = i % 2
    return remainder == 0

print("All numbers betweeen 0 and 20: even or not")
for i in range(20):
    if is_even(i):
        print(i, "even")
    else:
        print(i, "odd")
        
        
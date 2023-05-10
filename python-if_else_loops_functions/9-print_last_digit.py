#!/usr/bin/python3

def print_last_digit(number):
    lastDigit = 0

    if number < 0:
        lastDigit = number % -10
    else:
        lastDigit = number % 10
    
    print(lastDigit)
    return(lastDigit)

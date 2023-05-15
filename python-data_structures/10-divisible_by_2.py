#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newList = []
    for index in len(my_list):
        if my_list[index] % 2 == 0:
            newList[index] == True
        else:
            newList[index] == False
    return newList

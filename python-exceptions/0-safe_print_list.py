#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for x in range(x):
        try:
            print(my_list[x], end='')
            count +=1
        except:
            return count
        print()
    return count

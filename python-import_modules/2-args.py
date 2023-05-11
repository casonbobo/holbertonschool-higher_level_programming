#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = 0
    num_arguments = len(sys.argv) - 1
    arguments = sys.argv[1:]
    if num_arguments == 0:
        print("0 arguments.")
    elif num_arguments == 1:
        print("1 argument:")
        for arg in arguments:
            print(count++ + ": " + arg)
    else:
        print(f"Number of arguments: {num_arguments}")
        for arg in arguments:
            print(count++ + ": " + arg)

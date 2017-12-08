#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    total = 0
    for i in range(1, len(args)):
        total = total + int(args[i])
    print('{}'.format(total))

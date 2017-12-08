#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    argc = len(args) - 1
    if argc == 0:
        print('{} arguments.'.format(argc))
    elif argc == 1:
        print('{} argument:'.format(argc))
    else:
        print('{:d} arguments:'.format(argc))
    for i in range(1, len(args)):
        print('{}: {}'.format(i, args[i]))

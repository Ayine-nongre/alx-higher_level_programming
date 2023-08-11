#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("{:d} arguments".format(len(sys.argv) - 1), end="")
        print(".")
    else:
        if len(sys.argv) == 2:
            print("{:d} argument".format(len(sys.argv) - 1), end="")
        else:
            print("{:d} arguments".format(len(sys.argv) - 1), end="")
        print(":")

        x = 1
        for i in (sys.argv)[1:]:
            print("{:d}: {:s}".format(x, i))
            x = x + 1

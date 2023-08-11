#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    print("{:d} arguments".format(len(sys.argv) - 1), end="")
    if len(sys.argv) == 1:
        print(".")
    else:
        print(":")

        x = 1
        for i in (sys.argv)[1:]:
            print("{:d}: {:s}".format(x, i))
            x = x + 1

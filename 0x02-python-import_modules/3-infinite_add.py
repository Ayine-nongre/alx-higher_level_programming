#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    ans = 0
    if len(sys.argv) == 1:
        print("{:d}".format(ans))
    else:
        for i in (sys.argv)[1:]:
            ans = ans + int(i)
        print("{:d}".format(ans))

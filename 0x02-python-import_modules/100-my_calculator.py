#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import calculator_1 as calc

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int((sys.argv)[1])
    b = int((sys.argv)[3])

    if (sys.argv)[2] == "+":
        ans = calc.add(a, b)
        print("{:d} + {:d} = {:d}".format(a, b, ans))
    elif (sys.argv)[2] == "-":
        ans = calc.sub(a, b)
        print("{:d} - {:d} = {:d}".format(a, b, ans))
    elif (sys.argv)[2] == "*":
        ans = calc.mul(a, b)
        print("{:d} * {:d} = {:d}".format(a, b, ans))
    elif (sys.argv)[2] == "/":
        ans = calc.add(a, b)
        print("{:d} / {:d} = {:d}".format(a, b, ans))
    elif sys.argv[2] != "+" and sys.argv[2] != "-" and sys.argv[2] != "*"
    and sys.argv[2] != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

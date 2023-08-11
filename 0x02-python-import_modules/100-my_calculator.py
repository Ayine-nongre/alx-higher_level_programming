#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import calculator_1 as calc

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int((sys.argv)[1])
    b = int((sys.argv)[3])
    sign = sys.argv[2]

    if sign == "+":
        ans = calc.add(a, b)
        print("{:d} + {:d} = {:d}".format(a, b, ans))
    elif sign == "-":
        ans = calc.sub(a, b)
        print("{:d} - {:d} = {:d}".format(a, b, ans))
    elif sign == "*":
        ans = calc.mul(a, b)
        print("{:d} * {:d} = {:d}".format(a, b, ans))
    elif sign == "/":
        ans = calc.add(a, b)
        print("{:d} / {:d} = {:d}".format(a, b, ans))
    elif sign != "+" and sign != "-" and sign != "*" and sign != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

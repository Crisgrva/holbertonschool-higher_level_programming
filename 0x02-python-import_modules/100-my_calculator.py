#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as calc
    message = "Unknown operator. Available operators: +, -, * and /"
    argc = len(sys.argv)

    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    sign = sys.argv[2]

    if sign != "+" and sign != "-" and sign != "*" and sign != "/":
        print("{}".format(message))
        exit(1)

    operand = sys.argv[1] + " " + sys.argv[2] + " " + sys.argv[3]

    if sign == "+":
        result = calc.add(int(sys.argv[1]), int(sys.argv[3]))
    elif sign == "-":
        result = calc.sub(int(sys.argv[1]), int(sys.argv[3]))
    elif sign == "*":
        result = calc.mul(int(sys.argv[1]), int(sys.argv[3]))
    elif sign == "/":
        result = calc.div(int(sys.argv[1]), int(sys.argv[3]))
    print("{} = {}".format(operand, result))

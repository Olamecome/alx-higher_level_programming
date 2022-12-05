#!/usr/bin/python3

import sys
from calculator_1 import add, sub, div, mul


if __name__ == "__main__":
    """
    Calculates operation based on operands

    Returns:
        1 for failure

    """

    if len(sys.argv[1:]) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return (1)

    if (sys.argv[2] not in ["+", "-", "*", "/"]):
        print("Unknown operator. Available operators: +, -, * and /")
        return (1)

    result = add(int(sys.argv[1]), int(sys.argv[3])) if sys.argv[2] == "+"
    else sub(int(sys.argv[1]), int(sys.argv[3])) if sys.argv[2] == "-"
    else mul(int(sys.argv[1]), int(sys.argv[3])) if sys.argv[2] == "*"
    else div(int(sys.argv[1]), int(sys.argv[3])) if sys.argv[2] == "/"

    print("{} {} {} = {}".
          format(sys.argv[1], sys.argv[2], sys.argv[3], result))

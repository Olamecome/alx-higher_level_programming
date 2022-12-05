#!/usr/bin/python3

import sys


def main():
    args = len(sys.argv) - 1

    sum = 0

    for num in sys.argv[1:]:
        sum += int(num)

    print(sum)

if __name__ == "__main__":
    main()

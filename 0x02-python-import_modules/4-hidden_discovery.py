#!/usr/bin/python3

import hidden_4


def main():

    names = dir(hidden_4)
    for name in names:
        print(name if name[:2] != "__")


if __name__ == "__main__":
    main()

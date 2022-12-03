#!/usr/bin/python3

import sys


def main():
    args = len(sys.argv) - 1

    print("{} argument{}"
          .format(args,
                  ("s:" if args > 1 else ":"
                   if args == 1 else "s.")))

    for item in sys.argv[1:]:
        print("{}: {}".format(sys.argv.index(item), item))


if __name__ == "__main__":
    main()

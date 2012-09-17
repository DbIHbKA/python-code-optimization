#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint


def main():
    for num in [8000, 16000, 32000, 64000]:
        filename = "{0}Kint.txt".format(num / 1000)
        with open(filename, "w") as f:
            f.writeline(num)
            for x in range(num):
                f.write(randint(-100000, 100000))


if __name__ == '__main__':
    main()

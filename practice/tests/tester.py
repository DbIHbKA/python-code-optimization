#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint


def main():
    for num in [1000, 2000, 4000, 8000, 16000, 32000, 64000]:
        filename = "{0}Kint.txt".format(num // 1000)
        with open(filename, "w") as f:
            f.write(str(num) + '\n')
            temp = set()
            while len(temp) < num:
                temp.add(str(randint(-100000, 100000)))
            f.write(' '.join(list(temp)))


if __name__ == '__main__':
    main()

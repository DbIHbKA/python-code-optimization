#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function


def read(filename):
    with open(filename) as f:
        n = int(f.readline())
        data = list(map(int, f.readline().split(' ')))
    return n, data


def main():
    n, data = read('../tests/8int.txt')
    count = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if data[i] + data[j] + data[k] == 0:
                    print(data[i], data[j], data[k])
                    count += 1
    return count


if __name__ == '__main__':
    print(main())

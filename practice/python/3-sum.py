#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function


def read(filename):
    with open(filename) as f:
        n = int(f.readline())
        data = list(map(int, f.readline().split(' ')))
    return n, data


def bin_search(a, x):
    first = 0
    last = len(a)
    while first < last:
        mid = first + (last - first) // 2
        if x <= a[mid]:
            last = mid
        else:
            first = mid + 1
    if last < len(a) and a[last] == x:
        return True
    else:
        return False


def main():
    n, data = read('../tests/8int.txt')
    data.sort()
    print(data)
    count = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            if bin_search(data[j + 1:], -(data[i] + data[j])):
                print(data[i], data[j], -(data[i]+data[j]))
                count += 1
    return count


if __name__ == '__main__':
    print(main())

#!/usr/bin/python
import math
import random


def divide(a, p, r):
    pivot = a[r]
    j = p
    i = p - 1
    while (j <= r):
        if a[j] > pivot:
            i = i + 1
            tmp = a[j]
            a[j] = a[i]
            a[i] = tmp
        j = j + 1
    tmp = a[i+1]
    a[i+1] = a[r]
    a[r] = tmp
    return i + 1
def quick_sort(a, p, r):
    if p < r:
        q = divide(a, p, r)
        quick_sort(a, p, q -1)
        quick_sort(a, q + 1, r)


if __name__ == "__main__":
    a = []
    for i in range(10):
       a.append(int(round(100 * random.random())))
    print a
    quick_sort(a, 0, len(a) - 1)
    print a

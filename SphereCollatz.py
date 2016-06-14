#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

import sys

CACHE = {1:1}
MAX_VALUE = 837799
MAX_CYCLE_LENGTH = 525
# ------------
# collatz_read
# ------------

def collatz_read(line):
    """
    read two ints
    line a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    nums = line.split()
    return [int(nums[0]), int(nums[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval(low, high):
    """
    low the beginning of the range, inclusive
    high the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    assert low > 0
    assert high > 0
    if low > high:
        temp = high
        high = low
        low = temp
    if low < (high//2+1):
        low = high//2+1
    if low <= MAX_VALUE <= high:
        return MAX_CYCLE_LENGTH
    max_result = 0
    for num in range(low, high+1):
        if num in CACHE:
            result = CACHE[num]
        else:
            result = cycle_length(num)
        if result > max_result:
            max_result = result
    return max_result


# ------------
# cycle_length
# ------------

def cycle_length(num):
    """
    return the cycle length of the num
    """
    assert num > 0
    if num == 1:
        return 1
    else:
        if num not in CACHE:
            if num%2==0:
                CACHE[num] = 1+cycle_length(num//2)
            else:
                CACHE[num] = 2+cycle_length(num+(num>>1)+1)
        return CACHE[num]


# -------------
# collatz_print
# -------------


def collatz_print(writer, low, high, val):
    """
    print three ints
    writer a writer
    low the beginning of the range, inclusive
    high the end       of the range, inclusive
    val the max cycle length
    """
    writer.write(str(low) + " " + str(high) + " " + str(val) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    for line in reader:
        if not line.strip():
            break
        low, high = collatz_read(line)
        val = collatz_eval(low, high)
        collatz_print(writer, low, high, val)

# -------------
# main
# -------------

if __name__ == "__main__":
    collatz_solve(sys.stdin, sys.stdout)
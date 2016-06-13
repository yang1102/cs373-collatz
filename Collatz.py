#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------


CACHE = {1:1}

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
    if low > high:
        temp = high
        high = low
        low = temp
    if low < (high//2+1):
        low = high//2+1

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
    global CACHE
    tempdic = {}
    lnum = []
    result = 1
    temp = num
    while temp!=1:
        if temp in CACHE:
            result += CACHE[temp]-1
            break
        else:
            if  temp%2==0:
                temp = temp//2
                result+=1
            else:
                temp = temp + (temp>>1) + 1
                result+=2
                tempdic[temp]=result
                lnum.append(temp)
    CACHE[num] = result
    for i in lnum:
        CACHE[i] = result - tempdic[i]+1
    return result


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
        if line in ['\n','\r\n']:
            break
        low, high = collatz_read(line)
        val = collatz_eval(low, high)
        collatz_print(writer, low, high, val)

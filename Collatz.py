#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------


cache = {1:1}

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

def collatz_eval(low, up):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    if low > up:
        temp = up
        up = low
        low = temp
    if low < (up//2+1):
        low = up//2+1

    max_result = 0
    for num in range(low, up+1):
        if num in cache:
            result = cache[num]
        else:
            result = cycle_length(num)
        if result > max_result:
            max_result = result
    return max_result


def cycle_length(num):
    global dic
    global cache
    tempdic = {}
    lnum = []
    result = 1
    temp = num   
    while temp!=1:
        if temp in cache:
            result += cache[temp]-1
            break
        else:
            if  temp%2==0:
                temp = temp//2
                result+=1
            else:
                temp = temp + (temp>>1) + 1
                result+=2
                tempdic[temp]=result;
                lnum.append(temp)                
    cache[num] = result
    for i in lnum:
        cache[i] = result - tempdic[i]+1
    return result 


# -------------
# collatz_print
# -------------


def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(rd, wr):
    """
    rd a reader
    wr a writer
    """
    for line in rd:
        if line in ['\n','\r\n']:
            break
        low, up = collatz_read(line)
        val = collatz_eval(low, up)
        collatz_print(wr, low, up, val)

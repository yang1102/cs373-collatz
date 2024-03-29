#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read_1(self):
        line = "1 10\n"
        i, j = collatz_read(line)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    # Test read range
    def test_read_2(self):
        line = "1 999999\n"
        i, j = collatz_read(line)
        self.assertEqual(i,  1)
        self.assertEqual(j, 999999)

    # Test blank space
    def test_read_3(self):
        line = "100           200\n"
        i, j = collatz_read(line)
        self.assertEqual(i, 100)
        self.assertEqual(j, 200)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        val = collatz_eval(1, 10)
        self.assertEqual(val, 20)

    def test_eval_2(self):
        val = collatz_eval(100, 200)
        self.assertEqual(val, 125)

    def test_eval_3(self):
        val = collatz_eval(201, 210)
        self.assertEqual(val, 89)

    def test_eval_4(self):
        val = collatz_eval(900, 1000)
        self.assertEqual(val, 174)

    def test_eval_5(self):
        val = collatz_eval(5, 5)
        self.assertEqual(val, 6)

    # Test reversed number
    def test_eval_6(self):
        val = collatz_eval(6, 5)
        self.assertEqual(val, 9)

    def test_eval_7(self):
        val = collatz_eval(1, 1)
        self.assertEqual(val, 1)

    def test_eval_8(self):
        val = collatz_eval(1, 999999)
        self.assertEqual(val, 525)
    # Test zero

    def test_eval_9(self):
        with self.assertRaises(AssertionError):
            collatz_eval(0, 10)

    def test_eval_10(self):
        with self.assertRaises(AssertionError):
            collatz_eval(-4, -1)

    # -----
    # print
    # -----

    def test_print_1(self):
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    # Test if the number out of range
    def test_print_2(self):
        writer = StringIO()
        collatz_print(writer, 1, 999999, 525)
        self.assertEqual(writer.getvalue(), "1 999999 525\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    # test if the input is a blank line
    def test_solve2(self):
        reader = StringIO("\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), '')

    def test_solve3(self):
        reader = StringIO("100 199\n200 299\n300 399\n400 499\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "100 199 125\n200 299 128\n300 399 144\n400 499 142\n")


# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""

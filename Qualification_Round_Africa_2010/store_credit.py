#!/usr/bin/python
"""
Problem

You receive a credit C at a local store and would like to buy two items. You
first walk through the store and create a list L of all available items. From
this list you would like to buy two items that add up to the entire value of the
credit. The solution you provide will consist of the two integers indicating the
positions of the items in your list (smaller number first).

Input

The first line of input gives the number of cases, N. N test cases follow. For
each test case there will be:

One line containing the value C, the amount of credit you have at the store. One
line containing the value I, the number of items in the store. One line
containing a space separated list of I integers. Each integer P indicates the
price of an item in the store. Each test case will have exactly one solution.
Output

For each test case, output one line containing "Case #x: " followed by the
indices of the two items whose price adds up to the store credit. The lower
index should be output first.


Input:
3
100
3
5 75 25
200
7
150 24 79 50 88 345 3
8
8
2 1 9 4 4 56 90 3

Output:
Case #1: 2 3
Case #2: 1 4
Case #3: 4 5
"""

import sys
import os


TEMPLATE = 'Case #{0}: {1} {2}'


def read_file(fileobj):
  with open(fileobj) as fd:
    number_of_cases = int(fd.readline())
    while True:
      credit = int(fd.next())
      number_of_items = int(fd.next())
      list_of_items = [int(x) for x in fd.next().split()]
      yield credit, number_of_items, list_of_items


def buy_items(credit, number_of_items, list_of_items):
  return next((a+1, b+1)
      for a in range(number_of_items)
      for b in range(number_of_items)
      if a != b
      if list_of_items[a] + list_of_items[b] == credit)


def main(fileobj):
  case_number = 0
  for each in read_file(fileobj):
    case_number += 1
    items = buy_items(*each)
    print TEMPLATE.format(case_number, *items)


def tests():
  assert buy_items(100, 3, [5, 75, 25]) == (2, 3)
  assert buy_items(200, 7, [150, 24, 79, 50, 88, 345, 3]) == (1, 4)
  assert buy_items(8, 8, [2, 1, 9, 4, 4, 56, 90, 3]) == (4, 5)


if __name__ == '__main__':
  tests()
  fileobj = ' '.join(sys.argv[1:])
  if os.path.isfile(fileobj):
    main(fileobj)

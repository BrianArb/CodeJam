#!/usr/bin/env python
"""
Problem

You are given two vectors v1=(x1,x2,...,xn) and v2=(y1,y2,...,yn). The scalar
product of these vectors is a single number, calculated as x1y1+x2y2+...+xnyn.

Suppose you are allowed to permute the coordinates of each vector as you wish.
Choose two permutations such that the scalar product of your two new vectors is
the smallest possible, and output that minimum scalar product.

Input

The first line of the input file contains integer number T - the number of test
cases. For each test case, the first line contains integer number n. The next
two lines contain n integers each, giving the coordinates of v1 and v2
respectively. Output

For each test case, output a line

Case #X: Y where X is the test case number, starting from 1, and Y is the
minimum scalar product of all permutations of the two given vectors. Limits

Small dataset

T = 1000
1 < n < 8
-1000 < xi, yi < 1000

Large dataset

T = 10
100 < n < 800
-100000 < xi, yi < 100000

Sample

Input
2
3
1 3 -5
-2 4 1
5
1 2 3 4 5
1 0 1 0 1

Output
Case #1: -25
Case #2: 6
"""
import sys
import os

TEMPLATE = 'Case #{0}: {1}'


def smallest(list_a, list_b):
  """Minimum scalar product of all permutations of the two given vectors.

  Args:
    list_a: list of integers.
    list_b: list of integers.
  Returns:
    int
  """
  list_a = sorted(list_a)
  list_b = sorted(list_b, reverse=True)
  lenght = len(list_a)
  return sum([list_a[i] * list_b[i] for i in range(lenght)])


def read_file(fileobj):
  """Read in a file.

  Args:
    fileobj: Path to a input file.
  Yields:
    tuple with two list.
  """
  with open(fileobj) as file_descriptor:
    _ = file_descriptor.readline()
    while True:
      _ = int(file_descriptor.next())
      list_a = [int(c) for c in file_descriptor.next().split()]
      list_b = [int(c) for c in file_descriptor.next().split()]
      yield list_a, list_b


def tests():
  """Some simple tests."""
  list_a = [1, 3, -5]
  list_b = [-2, 4, 1]
  assert smallest(list_a, list_b) == -25
  list_a = [1, 2, 3, 4, 5]
  list_b = [1, 0, 1, 0, 1]
  assert smallest(list_a, list_b) == 6


def main():
  """Hooray for main."""
  fileobj = ' '.join(sys.argv[1:])

  if not os.path.isfile(fileobj):
    sys.exit(1)

  case_number = 0
  for list_a, list_b in read_file(fileobj):
    case_number += 1
    minimum_scalar = smallest(list_a, list_b)
    print TEMPLATE.format(case_number, minimum_scalar)


if __name__ == '__main__':
  tests()
  main()


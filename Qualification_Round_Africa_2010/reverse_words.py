#!/usr/bin/env python
"""
Problem

Given a list of space separated words, reverse the order of the words. Each line
of text contains L letters and W words. A line will only consist of letters and
space characters. There will be exactly one space character between each pair of
consecutive words.

Input

The first line of input gives the number of cases, N. N test cases follow. For
each test case there will a line of letters and space characters indicating a
list of space separated words. Spaces will not appear at the start or end of a
line.

Output

For each test case, output one line containing "Case #x: " followed by the list
of words in reverse order.

Limits

Small dataset

N = 5
1 < L < 25

Large dataset

N = 100
1 < L < 1000

Sample

Input 
3
this is a test
foobar
all your base

Output 
Case #1: test a is this
Case #2: foobar
Case #3: base your all
"""
import sys
import os

TEMPLATE = 'Case #{0}: {1}'

def main(fileobj):
  with open(fileobj) as fd:
    _number_of_cases = fd.readline()
    case_number = 0
    for line in fd.readlines():
      case_number += 1
      reverse_line = ' '.join(line.split()[::-1])
      print TEMPLATE.format(case_number, reverse_line)


def tests():
  case_1 = 'this is a test'.split()[::-1]
  case_2 = 'foobar'.split()[::-1]
  case_3 = 'all your base'.split()[::-1]
  assert case_1 == ['test', 'a', 'is', 'this']
  assert case_2 == ['foobar']
  assert case_3 == ['base', 'your', 'all']
  
  
if __name__ == '__main__':
  tests()
  fileobj = ' '.join(sys.argv[1:])
  if os.path.isfile(fileobj):
    main(fileobj)

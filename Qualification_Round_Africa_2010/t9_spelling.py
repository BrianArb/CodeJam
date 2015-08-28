#!/usr/bin/env python
"""
Problem

The Latin alphabet contains 26 characters and telephones only have ten digits on
the keypad. We would like to make it easier to write a message to your friend
using a sequence of keypresses to indicate the desired characters. The letters
are mapped onto the digits as shown below. To insert the character B for
instance, the program would press 22. In order to insert two characters in
sequence from the same key, the user must pause before pressing the key a second
time. The space character ' ' should be printed to indicate a pause. For
example, 2 2 indicates AA whereas 22 indicates B.

+------+-----+------+
|  1   |  2  |  3   |
|      | ABC | DEF  |
+------+-----+------+
|  4   |  5  |  6   |
| GHI  | JKL | MNO  |
+------+-----+------+
|   7  |  8  |  9   |
| PQRS | TUV | WXYZ |
+------+-----+------+
|  *   |  0  |  #   |
+------+-----+------+

Input

The first line of input gives the number of cases, N. N test cases follow. Each
case is a line of text formatted as

desired_message Each message will consist of only lowercase characters a-z and
space characters ' '. Pressing zero emits a space.

Output

For each test case, output one line containing "Case #x: " followed by the
message translated into the sequence of keypresses.

Limits

1 < N < 100.

Small dataset

1 < length of message in characters < 15.

Large dataset

1 < length of message in characters < 1000.

Sample
Input 
4
hi
yes
foo  bar
hello world

Output 
Case #1: 44 444
Case #2: 999337777
Case #3: 333666 6660 022 2777
Case #4: 4433555 555666096667775553
"""
import sys
import os

MAP_LETTER = {
    ' ': '0',
    'A': '2', 'B': '22', 'C': '222',
    'D': '3', 'E': '33', 'F': '333',
    'G': '4', 'H': '44', 'I': '444',
    'J': '5', 'K': '55', 'L': '555',
    'M': '6', 'N': '66', 'O': '666',
    'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
    'T': '8', 'U': '88', 'V': '888',
    'W': '9', 'X': '99', 'Y': '999', 'Z': '9999'}

TEMPLATE = 'Case #{0}: {1}'


def key_presses(string):
  return_value = ''
  for c in string.upper():
    digits = MAP_LETTER.get(c, None)
    if digits is None:
      continue
    if return_value.endswith(digits[0]):
      return_value += ' ' + digits
    else:
      return_value += digits
  return return_value


def tests():
  assert key_presses('hi') == '44 444'
  assert key_presses('yes') == '999337777'
  assert key_presses('foo  bar') == '333666 6660 022 2777'
  assert key_presses('hello world\n') == '4433555 555666096667775553'


def main(fileobj):
  with open(fileobj) as fd:
    _number_of_cases = fd.readline()
    case_number = 0
    for line in fd.readlines():
      case_number += 1
      string = key_presses(line)
      print TEMPLATE.format(case_number, string)


if __name__ == '__main__':
  tests()
  fileobj = ' '.join(sys.argv[1:])
  if os.path.isfile(fileobj):
    main(fileobj)

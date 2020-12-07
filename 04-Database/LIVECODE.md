# Database - Livecode

Today, our livecode is not about database. It's about **Algorithmic**!
Let's practise with the "colorful number" problem using **TDD**.


For a given number N find if it's a COLORFUL number or not :

A number can be broken into different contiguous sub-subsequence parts.
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
This number is a COLORFUL number, since product of every digit of a contiguous subsequence is different.

```
Example:

N = 23
2 3 23
2 -> 2
3 -> 3
23 -> 6
```
23 is a COLORFUL number since product of every digit of a sub-sequence are different.


## Setup

```bash
mkdir -p colorful && cd $_
pipenv --python 3.8
pipenv install nose
mkdir tests
touch colorful.py
touch tests/test_colorful.py

# We now can run:
pipenv run nosetests # => 0 tests for now
```

Bootstrap the testing class:

```python
# tests/test_colorful.py
import unittest

class ColorfulTest(unittest.TestCase):
    pass
```

## Solution

Please do not peek _before_ the livecode session!

<details><summary markdown="span">View solution
</summary>

```python
# test/test_colorful.py

import unittest
from colorful import is_colorful

class ColorfulTest(unittest.TestCase):
    def test_one_digit_number(self):
        self.assertTrue(is_colorful(0))
        self.assertTrue(is_colorful(1))
        self.assertTrue(is_colorful(2))
        self.assertTrue(is_colorful(3))
        self.assertTrue(is_colorful(4))
        self.assertTrue(is_colorful(5))
        self.assertTrue(is_colorful(6))
        self.assertTrue(is_colorful(7))
        self.assertTrue(is_colorful(8))
        self.assertTrue(is_colorful(9))

    def test_many_digits_number_with_at_least_one_digit_0_or_1(self):
        self.assertFalse(is_colorful(21))
        self.assertFalse(is_colorful(301))
        self.assertFalse(is_colorful(87610))
        self.assertFalse(is_colorful(1034))

    def test_many_digits_number_with_a_duplicate_digit(self):
        self.assertFalse(is_colorful(232))
        self.assertFalse(is_colorful(8797))
        self.assertFalse(is_colorful(34837))

    def test_colorful_number(self):
        self.assertTrue(is_colorful(23))
        self.assertTrue(is_colorful(3245))
```

```python
# colorful.py

def is_colorful(number):
    number_as_string = str(number)
    decomposed_number = [int(char) for char in number_as_string]
    number_as_set = set(decomposed_number)

    # Colorful if only one digit
    if number <=9:
        return True

    # Not colorful if digits 0 or 1 is present
    if "0" in number_as_string or "1" in number_as_string:
        return False

    # Not colorful if there is a duplicate digit
    if len(number_as_set) != len(number_as_string):
        return False

    # Main implementation
    i = 0
    j = 1
    n = len(number_as_string)

    val1 = 0
    val2 = 0

    while j < n :
        val1 = int(number_as_string[i])
        val2 = int(number_as_string[j])

        product_val = val1 * val2
        if product_val in number_as_set:
            return False

        number_as_set.add(product_val)

        i = i+1
        j = j+1

    return True
```

</details>

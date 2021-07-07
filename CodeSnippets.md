## Snippet on how to use the re.sub

```
import re
s = "from random import sample"
re.sub("[aeiou]", "*", s)
re.subn("[aeiou]", "*", s)
```

## Get a random sample of a range of numbers in Python

```
from random import sample
numbers = range(81,101)
for _ in range(3):
    print(sample(numbers, 5))
```
## Tempfile fetching
```
export TMPDIR=/tmp
import os
os.getenv("TMPDIR")

import tempfile
tempfile.gettempdir()
```
## Calling isalnum() on a string returns True if all the characters are alphanumeric [a-z0-9]
```
for s in 'pybites py@bites pybit.es pybitesl',split():
    print(s, s.isalnum())
```

## Using next value
```
import itertools
seq = itertools.count(11)
next(seq)
next(seq)

# Using step
seq = itertools.count(6, step=3)
for _ in range(3):
    next(seq)
    
seq = itertools.count(3.75, step=0.25)
for _ in range(3):
    next(seq)
```

## Reading the csv file
```
import csv
with open('names.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
```

## Get Close Matches
```
from difflib import get_close_matches
names = ['julian', 'pybites', 'bob', 'tim', 'python', 'sara', 'james', 'ana']
get_close_matches('pythonista', names)
```

## Password hiding
```
from getpass import getpass
password = getpass("and ypur password? ")
print(password)
```

## takewhile method
```
from itertools import takewhile
s = '1a2b3c4d5e6f'

def test_func(ch):
    return ch.isdigit() or ch in "ab"

list(takewhile(test_func,s))
```

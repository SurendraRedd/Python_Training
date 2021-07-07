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

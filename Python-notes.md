---
layout: post
---

# Python tutorials | Python阅读材料

[Python desciptor](https://realpython.com/python-descriptors/)

[Python super function](https://realpython.com/python-super/)

[Python @property](https://www.programiz.com/python-programming/property)

### Handy python commands:
1. Get the second field of a tab separated file and review the structure of the sample json file
```json
id1	{"key1":{"s_key":0},"key2":{"s_key":0}}
id2	{"key1":{"s_key":0},"key2":{"s_key":0}}
```

```bash
awk -F$'\t' '{print $2}' sample.json |  head -1 |  python -m json.tool
```

2. Bitwise operators. The order of bitwise operation is after PEMDAS.

```python
x << y # The same as x * 2**y
x >> y # The same as x // 2**y
~ z # The same as -x - 1

8 >> 2 + 2 # The result is 0 rather than 4
```

### PEP8 Summary:
1. Imports  

Imports should be grouped in the following order:  

  * Standard library imports.  
  * Related third party imports.  
  * Local application/library specific imports.  

You should put a blank line between each group of imports.  

```python
import re
import loggings

import pandas as pd

from mypackage import JonRunner
```
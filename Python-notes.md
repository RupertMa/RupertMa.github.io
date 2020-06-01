---
layout: post
---

# Python tutorials | Python阅读材料

[Python desciptor](https://realpython.com/python-descriptors/)

[Python super function](https://realpython.com/python-super/)

[Python @property](https://www.programiz.com/python-programming/property)

[Python try, except, else, finally](http://tutors.ics.uci.edu/index.php/79-python-resources/104-try-except)

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

3. Compare complex python object per your needs:  
A litter trick to make your life easier.  
```python
# Let's say you have a complex object like ListNode and you want to sort a list of them by their values
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

a = ListNode(-100)
b = ListNode()
a.next = b
print(a > b) # This will give you True

ListNode.__lt__ = lambda x, y : x.val < y.val # This line could be changed as per your needs.
print(a > b) # This will give you False
```  
[More readings about Python operator](https://docs.python.org/3.7/library/operator.html)


### PEP8 Summary:
1. Imports  

Imports should be grouped in the following order:  

  * Standard library imports.  
  * Related third party imports.  
  * Local application/library specific imports.  

You should put a blank line between each group of imports.  

```python
import re
import logging

import pandas as pd

from mypackage import JonRunner
```
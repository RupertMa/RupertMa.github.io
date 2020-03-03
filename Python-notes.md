---
layout: post
---

# Python tutorials | Python阅读材料

[Python desciptor](https://realpython.com/python-descriptors/)

[Python super function](https://realpython.com/python-super/)

### Handy python commands:
1. Get the second field of a tab separated file and review the structure of the sample json file
```json
id1	{"key1":{"s_key":0},"key2":{"s_key":0}}
id2	{"key1":{"s_key":0},"key2":{"s_key":0}}
```

```bash
awk -F$'\t' '{print $2}' sample.json |  head -1 |  python -m json.tool
```


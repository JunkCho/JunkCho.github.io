---
layout: posts
title: BOJ Test posting
categories:
  - 그 외
tags:
  - jeykll
  - github
  - markdown
---
```python
A = int(input())
B = i // 100 *100
temp = 0
if A <= 99:
    print(A)
elif A>= 1000:
    print(144)
else :
    for i in range(100, A+1):
        if (B - ((i - B) // 10)) == (i - 100 * B) // 10 - ((i - 100 * B) - (10 * ((i - 100 * B) // 10))):
            temp += 1
    print(temp+99)
```

# Arrays

+ [Megre two sorted arrays](#megre-two-sorted-arrays)
+ [Squares of sorted array](#squares-of-sorted-array)


## Megre two sorted arrays
```python
def merge(lst1, lst2):
    p1 = p2 = 0
    ans = []
    while p1 < len(lst1) and p2 < len(lst2):
        if lst2[p2] < lst1[p1]:
            ans.append(lst2[p2])
            p2 += 1
        else:
            ans.append(lst1[p1])
            p1 += 1
    ans.extend(lst1[p1:])
    ans.extend(lst2[p2:])
    return ans
```

## Squares of sorted array

```python
def squares(s):
    zero_index = bisect.bisect_left(s, 0)
    negative_numbers = s[zero_index - 1::-1]
    positive_numbers = s[zero_index:]
    return merge([x**2 for x in positive_numbers], [x**2 for x in negative_numbers])

```

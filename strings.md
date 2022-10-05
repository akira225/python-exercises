# Strings

+ [String compression](#string-compression)

## String compression

Compresses repeating chars of input string (given as a list of chars) (e.g. aabbbbbcddde -> a2b5cd3e)

```python
def compress(elems):
    if len(elems) == 0:
        return ""
    elif len(elems) == 1:
        return elems[0]
    elems.append("")
    prev = elems[0]
    count = 1
    ans = []
    for el in elems[1:]:
        if el == prev:
            count += 1
        else:
            if count > 1:
                ans.append(prev + str(count))
            else:
                ans.append(prev)
            count = 1
            prev = el

    return ''.join(ans)
```

# Matrices

+ [Diagonal sum](#diagonal-sum)

## Diagonal sum

Find sum of diagonal evlements of a matrix n x n 

```python
def diagonal_sum(mat):
    ans = 0
    n = len(mat)
    for i in range(n):
        ans += mat[i][i] + mat[i][n-i-1]
    if n % 2 == 1:
        ans -= mat[n//2][n//2]
    return ans
```

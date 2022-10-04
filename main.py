import bisect


def diagonal_sum(mat):
    """
    Compute the sum of diagonal values of a matrix n x n
    :param mat: list[list[int]]
    :return: int
    """
    ans = 0
    n = len(mat)
    for i in range(n):
        ans += mat[i][i] + mat[i][n-i-1]
    if n % 2 == 1:
        ans -= mat[n//2][n//2]
    return ans


def merge(lst1, lst2):
    """
    Merges two sorted lists
    :param lst1: list[int]
    :param lst2: list[int]
    :return: list[int]
    """
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


def squares(s):
    """
    Returns squared values of given sorted list of integers in sorted order
    :param s: list[int]
    :return: list[int]
    """
    zero_index = bisect.bisect_left(s, 0)
    negative_numbers = s[zero_index - 1::-1]
    positive_numbers = s[zero_index:]
    return merge([x**2 for x in positive_numbers], [x**2 for x in negative_numbers])


def compress(elems):
    """
    Compresses repeating chars of input string (e.g. aabbbbcdd -> a2b4cd2)
    :param elems: str
    :return: str
    """
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

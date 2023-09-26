"""Code for merging two sorted lists."""


def merge(x: list[int], y: list[int]) -> list[int]:
    """
    Merge two sorted lists.

    Returns a list that contains all the elements in x and y
    in sorted order.

    >>> merge([1, 2, 4, 6], [1, 3, 4, 5])
    [1, 1, 2, 3, 4, 4, 5, 6]
    """
    i, j = 0, 0 # 2
    z = [] # 1
    while i < len(x) and j < len(y): # 2n + 2m
        if x[i] < y[j]: #
            z.append(x[i]) #
            i += 1 #
        else:
            z.append(y[j])
            j += 1
    z += y[j:]
    z += x[i:]
    return z

print(merge([1, 2, 4, 6], [1, 3, 4, 5]))
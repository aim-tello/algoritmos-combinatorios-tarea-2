"""Ejercicio 2: busqueda binaria iterativa."""

from typing import Callable, Sequence


def binary_search_iterative(a: Sequence[int], x: int) -> int:
    """Busca ``x`` en ``a`` y retorna su indice, o -1 si no existe."""
    l = 0
    r = len(a) - 1

    while l <= r:
        m = l + (r - l) // 2

        if a[m] == x:
            return m

        if a[m] < x:
            l = m + 1
        else:
            r = m - 1

    return -1


BinarySearchIterative: Callable[[Sequence[int], int], int] = binary_search_iterative


def binary_search_recursive(a: Sequence[int], x: int, l: int, r: int) -> int:
    """Busca ``x`` recursivamente en ``a[l:r+1]`` y retorna su indice o -1."""
    if l > r:
        return -1

    m = l + (r - l) // 2

    if a[m] == x:
        return m

    if a[m] < x:
        return binary_search_recursive(a, x, m + 1, r)

    return binary_search_recursive(a, x, l, m - 1)


BinarySearchRecursive: Callable[[Sequence[int], int, int, int], int] = binary_search_recursive

"""Ejercicio 2: busqueda binaria iterativa."""

from typing import Callable, Sequence


def binary_search_iterative(a: Sequence[int], x: int) -> int:
    """Busca ``x`` en ``a`` y retorna su indice, o -1 si no existe."""
    # Justificación de Correctitud (Invariante de Ciclo):
    # En cada iteración, si $x \in A$, entonces necesariamente $x \in A[L ... R]$.
    # Al inicio, $L=0$ y $R=n-1$, lo cual cumple el invariante trivialmente.
    # En cada paso, si $A[M] < x$, por la propiedad de monotonicidad del arreglo,
    # $x$ no puede estar en $A[0 ... M]$, garantizando que el nuevo intervalo
    # $A[M+1 ... R]$ contiene a $x$. El argumento es análogo para el límite
    # superior. El ciclo termina estrictamente porque el tamaño del intervalo
    # $R - L + 1$ es estrictamente decreciente.
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
    # Justificación de Correctitud (Inducción Fuerte):
    # Para el caso base, si la longitud del arreglo es $0$ ($L > R$), el elemento
    # no existe y se retorna $-1$ correctamente. Supongamos por inducción que la
    # función es correcta para subarreglos de tamaño menor estricto a $k$. Para
    # un arreglo de tamaño $k$, calculamos $M$. Si $A[M] = x$, el algoritmo es
    # trivialmente correcto. Si no, genera una instancia del mismo problema
    # acotada en tamaño a un máximo de $\lfloor k/2 \rfloor$. Por la hipótesis
    # inductiva, esta llamada recursiva es correcta.
    if l > r:
        return -1

    m = l + (r - l) // 2

    if a[m] == x:
        return m

    if a[m] < x:
        return binary_search_recursive(a, x, m + 1, r)

    return binary_search_recursive(a, x, l, m - 1)


BinarySearchRecursive: Callable[[Sequence[int], int, int, int], int] = binary_search_recursive

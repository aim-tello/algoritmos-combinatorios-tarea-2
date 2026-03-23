"""Ejercicio 16: generacion de permutaciones para 3 <= n <= 6.

Se inicia con los vectores:
- X = (0, 1, ..., n-1): permutacion actual.
- M = (0, 1, ..., n-1): vector inverso (M[v] = posicion de v en X).
"""

from __future__ import annotations


def _next_permutation(x: list[int], m: list[int]) -> bool:
    """Avanza ``x`` a la siguiente permutacion lexicografica.

    Mantiene sincronizado el vector inverso ``m``.
    Retorna ``False`` cuando ``x`` ya esta en la ultima permutacion.
    """
    n = len(x)

    i = n - 2
    while i >= 0 and x[i] >= x[i + 1]:
        i -= 1
    if i < 0:
        return False

    j = n - 1
    while x[j] <= x[i]:
        j -= 1

    value_i = x[i]
    value_j = x[j]
    x[i], x[j] = value_j, value_i
    m[value_i], m[value_j] = j, i

    left = i + 1
    right = n - 1
    while left < right:
        value_left = x[left]
        value_right = x[right]
        x[left], x[right] = value_right, value_left
        m[value_left], m[value_right] = right, left
        left += 1
        right -= 1

    return True


def generate_permutations(n: int) -> list[tuple[int, ...]]:
    """Genera todas las permutaciones de tamano ``n``."""
    if n < 0:
        raise ValueError("n debe ser no negativo")

    x = list(range(n))
    m = list(range(n))

    permutations: list[tuple[int, ...]] = [tuple(x)]
    while _next_permutation(x, m):
        permutations.append(tuple(x))

    return permutations


def run_ejercicio_16() -> None:
    """Ejecuta la generacion para 3 <= n <= 6 e imprime resultados."""
    for n in range(3, 7):
        perms = generate_permutations(n)
        print(f"n={n} -> total={len(perms)}")
        for permutation in perms:
            print(permutation)
        print()


if __name__ == "__main__":
    run_ejercicio_16()

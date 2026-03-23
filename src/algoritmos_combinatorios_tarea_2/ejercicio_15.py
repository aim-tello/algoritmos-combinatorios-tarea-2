"""Ejercicio 15: calculo de permutacion por unranking lexicografico."""

from algoritmos_combinatorios_tarea_2.ejercicio_12 import perm_lex_unrank

N = 8
RANK = 32876


def solve_ejercicio_15() -> list[int]:
    """Calcula unrank(32876) para n=8 usando perm_lex_unrank."""
    return perm_lex_unrank(N, RANK)


if __name__ == "__main__":
    permutation = solve_ejercicio_15()
    print(f"unrank({RANK}) para n={N} = {permutation}")

# Resultado de ejecucion:
# unrank(32876) para n=8 = [7, 4, 5, 8, 6, 2, 1, 3]

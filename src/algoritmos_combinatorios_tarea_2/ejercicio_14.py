"""Ejercicio 14: calculo de rango lexicografico de una permutacion."""

from algoritmos_combinatorios_tarea_2.ejercicio_12 import perm_lex_rank

PERMUTATION = [6, 4, 5, 2, 7, 3, 8, 1]


def solve_ejercicio_14() -> int:
    """Calcula rank([6, 4, 5, 2, 7, 3, 8, 1]) usando perm_lex_rank."""
    n = len(PERMUTATION)
    return perm_lex_rank(n, PERMUTATION)


if __name__ == "__main__":
    rank_value = solve_ejercicio_14()
    print(f"rank({PERMUTATION}) = {rank_value}")

# Resultado de ejecucion:
# rank([6, 4, 5, 2, 7, 3, 8, 1]) = 27759

import math

import pytest

from algoritmos_combinatorios_tarea_2.ejercicio_12 import perm_lex_rank, perm_lex_unrank


@pytest.mark.parametrize(
    ("perm", "expected_rank"),
    [
        ([1, 2, 3], 0),
        ([1, 3, 2], 1),
        ([2, 1, 3], 2),
        ([2, 3, 1], 3),
        ([3, 1, 2], 4),
        ([3, 2, 1], 5),
    ],
)
def test_perm_lex_rank_known_values(perm: list[int], expected_rank: int) -> None:
    assert perm_lex_rank(3, perm) == expected_rank


@pytest.mark.parametrize("rank", [0, 1, 2, 3, 4, 5])
def test_perm_lex_unrank_known_values(rank: int) -> None:
    expected_perms = {
        0: [1, 2, 3],
        1: [1, 3, 2],
        2: [2, 1, 3],
        3: [2, 3, 1],
        4: [3, 1, 2],
        5: [3, 2, 1],
    }
    assert perm_lex_unrank(3, rank) == expected_perms[rank]


def test_rank_unrank_roundtrip_for_n4() -> None:
    n = 4
    for rank in range(math.factorial(n)):
        perm = perm_lex_unrank(n, rank)
        assert sorted(perm) == [1, 2, 3, 4]
        assert perm_lex_rank(n, perm) == rank

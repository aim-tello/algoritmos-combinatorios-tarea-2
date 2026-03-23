import pytest

from algoritmos_combinatorios_tarea_2.ejercicio_13 import prev_partition


@pytest.mark.parametrize(
    ("partition", "expected_previous"),
    [
        ([4, 1], [5]),
        ([3, 2], [4, 1]),
        ([3, 1, 1], [3, 2]),
        ([2, 2, 1], [3, 1, 1]),
        ([2, 1, 1, 1], [2, 2, 1]),
        ([1, 1, 1, 1, 1], [2, 1, 1, 1]),
    ],
)
def test_prev_partition_transitions(
    partition: list[int], expected_previous: list[int]
) -> None:
    assert prev_partition(partition) == expected_previous


@pytest.mark.parametrize("partition", [[5], [1]])
def test_prev_partition_returns_none_for_supreme_partition(partition: list[int]) -> None:
    assert prev_partition(partition) is None

import pytest

from algoritmos_combinatorios_tarea_2.ejercicio_2 import (
    BinarySearchIterative,
    BinarySearchRecursive,
)


@pytest.mark.parametrize(
    ("array", "target", "expected_index"),
    [
        ([1], 1, 0),
        ([1, 3, 5, 7, 9], 1, 0),
        ([1, 3, 5, 7, 9], 5, 2),
        ([1, 3, 5, 7, 9], 9, 4),
        ([2, 4, 6, 8, 10, 12], 8, 3),
    ],
)
def test_binary_search_iterative_found(
    array: list[int], target: int, expected_index: int
) -> None:
    assert BinarySearchIterative(array, target) == expected_index


@pytest.mark.parametrize(
    ("array", "target"),
    [
        ([], 3),
        ([1], 2),
        ([1, 3, 5, 7, 9], 0),
        ([1, 3, 5, 7, 9], 8),
        ([1, 3, 5, 7, 9], 10),
    ],
)
def test_binary_search_iterative_not_found(array: list[int], target: int) -> None:
    assert BinarySearchIterative(array, target) == -1


@pytest.mark.parametrize(
    ("array", "target", "expected_index"),
    [
        ([1], 1, 0),
        ([1, 3, 5, 7, 9], 1, 0),
        ([1, 3, 5, 7, 9], 5, 2),
        ([1, 3, 5, 7, 9], 9, 4),
        ([2, 4, 6, 8, 10, 12], 8, 3),
        ([], 3, -1),
        ([1], 2, -1),
        ([1, 3, 5, 7, 9], 0, -1),
        ([1, 3, 5, 7, 9], 8, -1),
        ([1, 3, 5, 7, 9], 10, -1),
    ],
)
def test_binary_search_recursive(
    array: list[int], target: int, expected_index: int
) -> None:
    assert BinarySearchRecursive(array, target, 0, len(array) - 1) == expected_index

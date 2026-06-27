import pytest

from app import get_age_category, get_numbers_sum, get_best_seller


@pytest.mark.parametrize(
    "age, expected",
    [
        (-1, "Некорректный возраст"),
        (10, "Ребенок"),
        (18, "Взрослый"),
        (30, "Взрослый"),
        (65, "Пенсионер"),
    ]
)
def test_get_age_category(age, expected):
    assert get_age_category(age) == expected


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 3], 6),
        ([10, -5, 5], 10),
        ([], 0),
        ([100], 100),
    ]
)
def test_get_numbers_sum(numbers, expected):
    assert get_numbers_sum(numbers) == expected


@pytest.mark.parametrize(
    "sales, expected",
    [
        ({"apple": 10, "banana": 5}, "apple"),
        ({"phone": 3, "laptop": 8, "tablet": 2}, "laptop"),
        ({}, None),
    ]
)
def test_get_best_seller(sales, expected):
    assert get_best_seller(sales) == expected
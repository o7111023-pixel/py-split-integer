from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    number = 23
    parts = 5

    result = split_integer(number, parts)

    assert sum(result) == number


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    number = 20
    parts = 5

    result = split_integer(number, parts)

    assert result == [4, 4, 4, 4, 4]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    number = 42
    parts = 1

    result = split_integer(number, parts)

    assert result == [number]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    number = 17
    parts = 4

    result = split_integer(number, parts)

    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    number = 3
    parts = 5

    result = split_integer(number, parts)

    assert result == [0, 0, 1, 1, 1]


def test_should_split_with_remainder_correctly() -> None:
    assert split_integer(10, 4) == [2, 2, 3, 3]


def test_should_split_with_remainder_correctly_second_case() -> None:
    assert split_integer(11, 4) == [2, 3, 3, 3]

from fizzbuzz.fizzbuzz import fizzbuzz


def test_fizzbuzz_returns_Fizz_when_number_divisible_by_three():
    assert fizzbuzz(3) == "Fizz"


def test_fizzbuzz_returns_a_number_when_it_is_not_divisble_by_three():
    assert fizzbuzz(4) == 4


def test_fizzbuzz_returns_Buzz_when_number_divisible_by_five():
    assert fizzbuzz(5) == "Buzz"

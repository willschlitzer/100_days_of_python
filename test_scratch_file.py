from scratch_file import hello_you, get_random_number, fizzbuz_input
import random
from unittest.mock import patch


def test_hello_you():
    assert hello_you("Mike") == "Hello Mike"


# Asserts a test patch object specifically for the randint method of the random class
@patch.object(random, "randint")
def test_get_random_number(m):
    # Decides what the "random" number is in this test
    m.return_value = 12
    # Conducts test
    assert get_random_number() == 12

def test_fizzbuz_input():
    assert fizzbuz_input(1) == 1
    assert fizzbuz_input(3) == "Fizz"
    assert fizzbuz_input(5) == "Buzz"
    assert fizzbuz_input(15) == "Fizz Buzz"

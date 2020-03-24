from scratch_file import hello_you, get_random_number
import random
from unittest.mock import patch


def test_hello_you():
    assert hello_you('Mike') == "Hello Mike"

@patch.object(random, 'randint')
def test_get_random_number(m):
    m.return_value=12
    assert get_random_number() == 12


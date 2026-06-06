import pytest

# Simple utility function to test
def is_adult(age):
    return age >= 18

@pytest.mark.parametrize("age, expected_result", [
    (15, False),
    (18, True),
    (21, True),
    (0, False)
])
def test_is_adult(age, expected_result):
    assert is_adult(age) == expected_result
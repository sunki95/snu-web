#test_pytest_func.py
from pytest_func import pytest_func

def test_pytest_func():
    assert pytest_func(4,5) == 9
    assert pytest_func(3,5) == 9

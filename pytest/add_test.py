import pytest
from add import *
def test_add():
    assert add(2,3) == 5

def test_fail():
    assert add(1,1) == 2

import pytest
from add import *

def add(x,y):
    return (x+y)

def test_add():
    assert add(2,3) == 5

def test_fail():
    assert add(1,1) == 2

def test_initial():
    amount = Amount()
    assert amount.balance == 0

def test_addamount():
    amount = Amount(100)
    assert amount.balance == 100

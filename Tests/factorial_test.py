import pytest
import factorial

def test_factorial():
    assert factorial.factorial(5)==120

def test_revers_fact():
    assert factorial.reverse_fact(120)=="5!"

def test_revers_fact():
    assert factorial.reverse_fact(3628800)=="10!"

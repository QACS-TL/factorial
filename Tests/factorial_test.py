import pytest
from Not_tests import notimportant

def test_fact():
    assert notimportant.fact(5)==120

def test_revers_fact():
    assert notimportant.reverse_fact(120)=="5!"

def test_revers_fact():
    assert notimportant.reverse_fact(3628800)=="10!"

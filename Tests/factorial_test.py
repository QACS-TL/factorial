import pytest
from Not_tests import notimportant

def test_fact():
    assert notimportant.fact(5)==120

def test_reverse_fact1():
    assert notimportant.reverse_fact(120)=="5!"

def test_reverse_fact2():
    assert notimportant.reverse_fact(3628800)=="10!"

def test_reverse_fact3():
    assert notimportant.reverse_fact(5040)=="7!"

def test_reverse_fact4():
    assert notimportant.reverse_fact(720)=="6!"

    

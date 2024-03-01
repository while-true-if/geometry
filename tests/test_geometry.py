import pytest

import geometry as gm

def test_pythagorean():
    assert gm.pythagorean(3,4,"x") == 5

def test_cie_heron():
    assert gm.cie_heron(0,0,5,0,5,12) == 30

def test_heron():
    assert gm.heron(5,12,13) == 30

def test_permutation():
    assert gm.permutation(7,3) == 210

def test_combination():
    assert gm.combination(7,3) == 35

"""
Description: Unit tests for IndexGenerator.
"""
# Copyright (c) 2024 - 2025 Milan Piskla
# Licensed under the MIT License - see LICENSE file for details

import pytest
from src.impl.indexer.IndexGenerator import IndexGenerator

def test_default():
    idxr = IndexGenerator()
    assert idxr.next() == 'a1'
    assert idxr.next() == 'a2'
    assert idxr.next() == 'a3'
    assert idxr.next() == 'a4'
    assert idxr.next() == 'a5'
    assert idxr.next() == 'a6'
    assert idxr.next() == 'a7'
    assert idxr.next() == 'a8'
    assert idxr.next() == 'a9'
    assert idxr.next() == 'aA'

def test_aZ():
    idxr = IndexGenerator('aZ')
    assert idxr.next() == 'aa'
    assert idxr.next() == 'ab'
    assert idxr.next() == 'ac'

def test_az():
    idxr = IndexGenerator('az')
    assert idxr.next() == 'b00'
    assert idxr.next() == 'b01'
    assert idxr.next() == 'b02'

def test_b0Z():
    idxr = IndexGenerator('b0Z')
    assert idxr.next() == 'b0a'
    assert idxr.next() == 'b0b'
    assert idxr.next() == 'b0c'

def test_b0z():
    idxr = IndexGenerator('b0z')
    assert idxr.next() == 'b10'
    assert idxr.next() == 'b11'
    assert idxr.next() == 'b12'

def test_bZz():
    idxr = IndexGenerator('bZz')
    assert idxr.next() == 'ba0'
    assert idxr.next() == 'ba1'
    assert idxr.next() == 'ba2'

def test_bzz():
    idxr = IndexGenerator('bzz')
    assert idxr.next() == 'c000'
    assert idxr.next() == 'c001'
    assert idxr.next() == 'c002'

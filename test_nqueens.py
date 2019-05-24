#test_nqueens.py

import pytest
from QueensTest1 import NQueens, main

def test_nqueens_result():
	assert main(8) == 92
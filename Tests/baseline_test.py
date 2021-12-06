import unittest
import sys
from baseline import baseline_removal
import numpy as np


def test_baseline_removal(): 

    test_data = np.array([1,1,1,1,1,1,1,1,1,1])
    answer = baseline_removal(test_data)
    correct = np.array([0,0,0,0,0,0,0,0,0,0])

    assert (answer==correct)



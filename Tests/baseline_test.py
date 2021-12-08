import unittest
import sys
from baseline import baseline_removal
from sklearn.linear_model import LinearRegression
import numpy as np


def test_baseline_removal(): 

    test_data = np.array([1,1,1,1,1,1,1,1,1,1])
    answer = baseline_removal(test_data)
    print(answer)
    correct = np.array([0,0,0,0,0,0,0,0,0,0])

    return np.testing.assert_array_equal(answer, correct, 'not equal bad bad bad')


if __name__=="__main__":
    
        answer = test_baseline_removal()
        print(answer)
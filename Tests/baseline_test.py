import unittest
import sys
from Code.baseline import baseline_removal, vandermonde_matrix,qr_factorization,linear_regression 
from sklearn.linear_model import LinearRegression # import LinearRegression
import numpy as np


def test_baseline_removal(): 

    #basic test 1, method should be able to return zero baseline
    test_data = np.array([1,1,1,1,1,1,1,1,1,1])
    answer = baseline_removal(test_data)
    correct = np.array([0,0,0,0,0,0,0,0,0,0])

    np.testing.assert_array_equal(answer, correct)

def test_vandermonde_matrix():

    test_data = np.ones(5)
    answer = vandermonde_matrix(test_data)
    correct = [[1,1,1],[1,2,4],[1,3,9],[1,4,16],[1,5,25]]
    
    np.testing.assert_array_equal(answer, correct)

def test_qr_factorization():

    test_data = [[1,1,1],[1,2,4],[1,3,9],[1,4,16],[1,5,25]]
    answer = np.round(qr_factorization(test_data),4)
    correct = np.round([[-6.32455532e-01,5.34522484e-01],[-3.16227766e-01,-2.67261242e-01],[8.32667268e-17,-5.34522484e-01],[3.16227766e-01,-2.67261242e-01],[6.32455532e-01,5.34522484e-01]], 4)
    print('qr', answer)
    np.testing.assert_array_equal(answer, correct)

def test_linear_regression():

    test_data = np.ones(5)
    qr_factorized = [[-6.32455532e-01,5.34522484e-01],[-3.16227766e-01,-2.67261242e-01],[8.32667268e-17,-5.34522484e-01],[3.16227766e-01,-2.67261242e-01],[6.32455532e-01,5.34522484e-01]]
    answer = linear_regression(test_data, qr_factorized)
    correct = np.ones(5)

    np.testing.assert_array_equal(answer, correct)

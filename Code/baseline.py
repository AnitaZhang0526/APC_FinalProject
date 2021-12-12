#required libraries are as follows: 
import numpy as np
from sklearn.linear_model import LinearRegression

"""
BaselineRemoval method takes an array of input data and returns the data with the baseline removed. 
BaselineRemoval uses an Ordinary Linear Regression method that fits to the QR-factorized Vandermonde matrix
This method is based on the process outlined in "Automated Method for Subtraction of Fluorescence from Biological Raman Spectra" by Lieber et al, 2003
This script was based on the imp
lementation available at: https://github.com/StatguyUser/BaselineRemoval
"""

def vandermonde_matrix(input_data):
        """
        A modified Vandermonde matrix is used in the subsequent linear regression to solve for a baseline.
        The generic Vandermonde matrix forms an NxN matrix that has i^m...i^(m-1)..i^(m-m)etc. for 1<i<N entries in input_data
        The final vandermonde_matrix is flipped horizontally, with the first column of 1's removed 
        """
        vander_columns = 3 #least squares linear regression requiring a degree of 2, hence we create a matrix of 3 columns and subsequently delete column of 1's 
        vander_rows = np.array((list(range(1,len(input_data)+1))))
        #vander_rows = np.array(vander_rows)      
        vandermonde_matrix = np.fliplr(np.vander(vander_rows, vander_columns))
        print('vander', vandermonde_matrix)
        return vandermonde_matrix
        
def qr_factorization(vandermonde_matrix):
        """
        QR factorization is performed to decompose the modified vandermonde matrix, A, into the product of two matricies, Q and R
        Q is an orthogonal matrix and R is an upper triangular matrix. 
        The Q matrix is used for fitting data to in the best-fit linear regression below. 
        The QR factorization of the Vandermonde matrix is required for generating the coefficients used in the least squares solution
        """
        qr_factorization = np.linalg.qr(vandermonde_matrix)[0][:,1:]
        print('qr', np.round(qr_factorization,4))
        return qr_factorization

def linear_regression(input_data, qr_factorization):

        #define number of loops performed in the final linear regression to evaluate a baseline
        iterative_loops = 100       
        #define placeholders for storing iterations of computed values for the computed baseline
        working = input_data
        prediction =[]        

        """
        Ordinary Least-Squares Linear Regression is performed on the input data by fitting it to the Q matrix generated above
        LinearRegression fits a linear model to minimize the residual sum of squares between observed targets in the dataset and those predicted by the linear approximation
        Predict is used to generate predicted labels for the trained model made by the LinearRegression().fit() method
        """
        #begin linear regression to evaluate baseline
        for i in range(iterative_loops):
             #LinearRegression()np.linalg.lstsq
            prediction=LinearRegression().fit(qr_factorization,working).predict(qr_factorization)
            working=np.array(np.minimum(input_data, prediction))
          
        #compute final baseline-removed data           
        final_data=np.array(prediction) 
        print('final data', final_data)
        return final_data
    
def baseline_removal(input_data):
        """
        Final baseline removal function returns the input_data minus the calculated baseline. 
        """
        vander = vandermonde_matrix(input_data)
        qr_factored = qr_factorization(vander)
        baseline = input_data - linear_regression(input_data,qr_factored)
        print('baseline', baseline)

        #return baseline-removed data 
        return baseline


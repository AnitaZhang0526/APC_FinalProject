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

def baseline_removal(input_data):
        
        #define number of loops performed in the final linear regression to evaluate a baseline
        iterative_loops = 100 
      
        """
        A modified Vandermonde matrix is used in the subsequent linear regression to solve for a baseline.
        The generic Vandermonde matrix forms an NxN matrix that has i^m...i^(m-1)..i^(m-m)etc. for 1<i<N entries in input_data
        The final vandermonde_matrix is flipped horizontally, with the first column of 1's removed 
        """
        vander_columns = 3 #least squares linear regression requiring a degree of 2, hence we create a matrix of 3 columns and subsequently delete column of 1's 
        vander_rows = np.array((list(range(1,len(input_data)+1))))
        #vander_rows = np.array(vander_rows)      
        vandermonde_matrix = np.fliplr(np.vander(vander_rows, vander_columns))

        """
        QR factorization is performed to decompose the modified vandermonde matrix, A, into the product of two matricies, Q and R
        Q is an orthogonal matrix and R is an upper triangular matrix. 
        The Q matrix is used for fitting data to in the best-fit linear regression below. 
        The QR factorization of the Vandermonde matrix is required for generating the coefficients used in the least squares solution
        """
        qr_factorization = np.linalg.qr(vandermonde_matrix)[0][:,1:]
      
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
            
            prediction=LinearRegression().fit(qr_factorization,working).predict(qr_factorization)
            working=np.array(np.minimum(input_data, prediction))
          
        #compute final baseline-removed data           
        baseline=np.array(input_data-prediction)
       
        #return baseline-removed data 
        return baseline
    

##for testing purposes, __main__ provided below: 
# if __name__=="__main__":

#          input_array = [1,1,1,1,1,1,1,1,1,1,1,1]
#          Modpoly_output = BaselineRemoval(input_array) #ftir class hardcodes this array and creates this object 
#          print('Original input:',input_array)
#          print('Modpoly base corrected values:',Modpoly_output)
 
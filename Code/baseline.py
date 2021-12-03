import numpy as np
import pandas as pd
import scipy.linalg as LA
from sklearn.linear_model import LinearRegression

import math
print("  fml ")
import sys


class BaselineRemoval():
    '''input_array: A pandas dataframe column provided in input as dataframe['input_df_column']. It can also be a Python list object
    degree: Polynomial degree
    '''     
    def __init__(self,input_array):
        self.input_array=input_array
        self.lin=LinearRegression()

    def poly(self,input_array_for_poly,degree_for_poly):
        
        input_array_for_poly = np.array(input_array_for_poly)
        
        X = np.transpose(np.vstack((input_array_for_poly**k for k in range(degree_for_poly+1))))  #here we are adding a row, but the power is ^0 for the first set so we just get 1's 
                
        return np.linalg.qr(X)[0][:,1:]


    def ModPoly(self,degree=2,repitition=100,gradient=0.001):
       
        criteria=np.inf

        baseline=[]
        corrected=[]

        ywork=self.input_array
        yold=self.input_array
        yorig=self.input_array #probably uneccessary since we already have it saved as self.input_array

        polx=self.poly(list(range(1,len(yorig)+1)),degree)
       
        nrep=0

        while (criteria>=gradient) and (nrep<=repitition):
            print("linfit", self.lin.fit(polx,yold)) #predict using a matrix of squaares??
            ypred=self.lin.fit(polx,yold).predict(polx)
            print("ypred is", ypred)

            ywork=np.array(np.minimum(yorig,ypred))
            criteria=sum(np.abs((ywork-yold)/yold))
            yold=ywork
            nrep+=1
        corrected=yorig-ypred
        corrected=np.array(list(corrected))
    
        return corrected
    

if __name__=="__main__":
#def execute(): 
        input_array = [1,2,5,62,24,663]
        #input_array = np.random.randint(0, 5, 10)
        obj = BaselineRemoval(input_array) #ftir class hardcodes this array and creates this object 
        Modpoly_output=obj.ModPoly(2)
        print('Original input:',input_array)
        print('Modpoly base corrected values:',Modpoly_output)
        





# banana = pd.read_excel('Book1.xlsx', converters={'wavenumber':float, 'intensity':float, 'baselineintensity':float})  
# y= banana["baselineintensity"]
# print("testing")
# answer=isinstance(y[1],float)
# print(answer)
# print("tested")


# #---------------actually stolen code-----
# def baseline(y, deg=None, max_it=None, tol=None):

#     """
#     Computes the baseline of a given data.

#     Iteratively performs a polynomial fitting in the data to detect its
#     baseline. At every iteration, the fitting weights on the regions with
#     peaks are reduced to identify the baseline only.

#     Parameters
#     ----------
#     y : ndarray
#         Data to detect the baseline.
#     deg : int (default: 3)
#         Degree of the polynomial that will estimate the data baseline. A low
#         degree may fail to detect all the baseline present, while a high
#         degree may make the data too oscillatory, especially at the edges.
#     max_it : int (default: 100)
#         Maximum number of iterations to perform.
#     tol : float (default: 1e-3)
#         Tolerance to use when comparing the difference between the current
#         fit coefficients and the ones from the last iteration. The iteration
#         procedure will stop when the difference between them is lower than
#         *tol*.

#     Returns
#     -------
#     ndarray
#         Array with the baseline amplitude for every original point in *y*
#     """
#     # for not repeating ourselves in `envelope`
#     if deg is None: deg = 3
#     if max_it is None: max_it = 100
#     if tol is None: tol = 1e-3
    
#     order = deg + 1
#     coeffs = np.ones(order)

#     # try to avoid numerical issues
#     cond = math.pow(abs(y).max(), 1. / order)
#     x = np.linspace(0., cond, y.size)
#     base = y.copy()

#     vander = np.vander(x, order)
#     vander_pinv = LA.pinv2(vander)

#     for _ in range(max_it):
#         coeffs_new = np.dot(vander_pinv, y)

#         if LA.norm(coeffs_new - coeffs) / LA.norm(coeffs) < tol:
#             break

#         coeffs = coeffs_new
#         base = np.dot(vander, coeffs)
#         y = np.minimum(y, base)

#     return base

# def envelope(y, deg=None, max_it=None, tol=None):
#     """
#     Computes the upper envelope of a given data.
#     It is implemented in terms of the `baseline` function.
    
#     Parameters
#     ----------
#     y : ndarray
#         Data to detect the baseline.
#     deg : int
#         Degree of the polynomial that will estimate the envelope.
#     max_it : int
#         Maximum number of iterations to perform.
#     tol : float
#         Tolerance to use when comparing the difference between the current
#         fit coefficients and the ones from the last iteration.

#     Returns
#     -------
#     ndarray
#         Array with the envelope amplitude for every original point in *y*
#     """
#     return y.max() - baseline(y.max() - y, deg, max_it, tol)


# fixed_data = envelope(y, deg=None, max_it=None, tol=None)
# print(fixed_data)
# a = np.array([[1,4,2],[7,9,4],[0,6,2]])
# np.savetxt('myfile.csv', fixed_data, delimiter=',')


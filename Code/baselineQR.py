import numpy as np
import pandas as pd
import scipy.linalg as LA
from sklearn.linear_model import LinearRegression

import warnings
warnings.filterwarnings('ignore')
"""definitely need to cite my sources here"""


#def (readfile) - to go into the ABC 

class BaselineRemoval():   #(probably dont need a class if this is all in main, 
# which will become one def method anyway)

    # def __init__(self,input_data):
    #     self.input_data = np.array(input_data)
    #     print(self.input_data)
    #     self.vander_degree  = 2
    #     #self.error = 0.001
    #     self.loops = 100
    # def __init__(self,input_data):
    #     self.lin=LinearRegression()
    #     self.input_data=input_data

    def BaselineRemoval(inputdata):

        input_data = np.array(inputdata)
        #vander_degree  = 2
        #self.error = 0.001
        loops = 100
        print(len(input_data))
                #make a list from 1 to N of the total # of entries in the dataset
        # length_data = list(range(1,len(input_data)))
        vandermonde_matrix=np.vander(list(range(0,len(input_data))),3)
        vandermonde_matrix=np.fliplr(vandermonde_matrix)
        
        # print(length_data)
        # for i in range(vander_degree+1): #why is it plus 1
        #     temp = np.power(length_data,i)
        #     vandermonde_matrix.append(temp) #
        print('vander is',vandermonde_matrix)

        print(np.linalg.qr(vandermonde_matrix)[0][:,1:])
        qr_factorized = np.linalg.qr(vandermonde_matrix)[0][:,1:]

        old_data = input_data
        baseline = []
        predicted_data = []

        for i in range(loops):
                predicted_data = LinearRegression().fit(qr_factorized,old_data).predict(old_data) #LinearRegression().fit(qr_factorized,old_data).predict(qr_factorized)
                old_data = np.array(np.minimum(input_data,predicted_data))
        baseline = old_data
        return baseline

if __name__=="__main__":
        input_data = ([35,134,1,123,42,22,22])
        print(input_data)
        baseline = BaselineRemoval.BaselineRemoval(input_data)
        print('baseline is',baseline)

import numpy as np
#import pandas as pd
#import scipy.linalg as LA
from sklearn.linear_model import LinearRegression

#import warnings
#warnings.filterwarnings('ignore')
#"""definitely need to cite my sources here"""


# def BaselineRemoval(input_data):
        
#         vander_columns = 3
#         iterative_loops = 100
#         error = 0.001
#         criteria=np.inf

#         #building Vandermonde Matrix 

#         vander_rows = (list(range(1,len(input_data)+1)))
#         vander_rows = np.array(vander_rows)
#         vandermonde_matrix = np.transpose(np.vstack((vander_rows**i for i in range(vander_columns))))
#         qr_factorization = np.linalg.qr(vandermonde_matrix)[0][:,1:]

#         counter=0
#         working = input_data
#         old = input_data
#         prediction =[]        
#         baseline=[]
        
#         # ywork=input_array
#         # yold=input_array
#         # yorig=input_array
      
#         # temp = 
#         # input_array_for_poly = np.array(temp)
#         # X = np.transpose(np.vstack((input_array_for_poly**k for k in range(vander_size))))
#         # polx = np.linalg.qr(X)[0][:,1:] 
#         # nrep=0

#         while (criteria>=error) and (counter<=iterative_loops):
            
#             prediction=LinearRegression().fit(qr_factorization,old).predict(qr_factorization)
            
#             working=np.array(np.minimum(input_data, prediction))
#             criteria=sum(np.abs((working-old)/old))
#             old=working
#             counter+=1
#         baseline=input_data-prediction
#         baseline=np.array(list(baseline))
    
#         return baseline
    

# if __name__=="__main__":
# #def execute(): 
#         input_array = [1,2,5,62,24,663]
#         #input_array = np.random.randint(0, 5, 10)
#         Modpoly_output = BaselineRemoval(input_array) #ftir class hardcodes this array and creates this object 
#         #Modpoly_output=obj.ModPoly(2)
#         print('Original input:',input_array)
#         print('Modpoly base corrected values:',Modpoly_output)
 
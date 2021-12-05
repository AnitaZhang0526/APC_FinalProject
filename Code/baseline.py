import numpy as np
#import pandas as pd
#import scipy.linalg as LA
from sklearn.linear_model import LinearRegression

#import warnings
#warnings.filterwarnings('ignore')
"""definitely need to cite my sources here"""


def BaselineRemoval(input_data):
        
        vander_columns = 3
        iterative_loops = 100
        #error = 0.001
        #criteria=np.inf

        #building Vandermonde Matrix 

        vander_rows = (list(range(1,len(input_data)+1)))
        vander_rows = np.array(vander_rows)
        vandermonde_matrix = np.transpose(np.vstack((vander_rows**i for i in range(vander_columns))))
        
        #qr factorization stuff here

        qr_factorization = np.linalg.qr(vandermonde_matrix)[0][:,1:]

        #counter=0
        
        #baseline ilnear regression fitting 
        
        working = input_data
        old = input_data
        prediction =[]        
        baseline=[]
        
        
        for i in range(iterative_loops):
            
            prediction=LinearRegression().fit(qr_factorization,old).predict(qr_factorization)
            
            working=np.array(np.minimum(input_data, prediction))
            #criteria=sum(np.abs((working-old)/old))
            old=working
            #counter+=1
        baseline=input_data-prediction
        baseline=np.array(list(baseline))
    
        return baseline
    

if __name__=="__main__":
#def execute(): 
        input_array = [1,2,5,62,24,663]
        #input_array = np.random.randint(0, 5, 10)
        Modpoly_output = BaselineRemoval(input_array) #ftir class hardcodes this array and creates this object 
        #Modpoly_output=obj.ModPoly(2)
        print('Original input:',input_array)
        print('Modpoly base corrected values:',Modpoly_output)
 
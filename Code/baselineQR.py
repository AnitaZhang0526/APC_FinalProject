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

    def BaselineRemoval(input_data):

        input_data = np.array(input_data)
        #vander_degree  = 2
        #self.error = 0.001
        loops = 100
        print(len(input_data))
                #make a list from 1 to N of the total # of entries in the dataset
        # length_data = list(range(1,len(input_data)))
        vandermonde_matrix=np.vander(list(range(1,len(input_data))))
        vandermonde_matrix=np.fliplr(vandermonde_matrix)
        
        # print(length_data)
        # for i in range(vander_degree+1): #why is it plus 1
        #     temp = np.power(length_data,i)
        #     vandermonde_matrix.append(temp) #
        print('vander is',vandermonde_matrix)

        print(np.linalg.qr(vandermonde_matrix))
        qr_factorized = np.linalg.qr(vandermonde_matrix)[0][:,1:]

        old_data = input_data
        baseline = []
        predicted_data = []
                

        for i in range(loops):
                predicted_data = LinearRegression.fit(qr_factorized,old_data).predict(qr_factorized)
                old_data = np.data(np.minimum(input_data,predicted_data))
        baseline = old_data
        return baseline

if __name__=="__main__":
        input_data = ([35,134,1,123,42])
        print(input_data)
        baseline = BaselineRemoval.BaselineRemoval(input_data)
        print(baseline)


    # def vandermonde(self): 
        
    #     vandermonde_matrix=[]
    #     #make a list from 1 to N of the total # of entries in the dataset
    #     length_data = list(range(1,len(self.input_data)))
    #     for i in range(self.vander_degree+1): #why is it plus 1
    #         temp = length_data**i
    #         vandermonde_matrix=np.hstack([vandermonde_matrix,temp]) #
    #         print(vandermonde_matrix)
    #     return vandermonde_matrix

        
        #currently just returning the exact section that we want, after creating our vandermonde array
    # def qr_factorization(vandermonde_matrix):
    #     #need to pass my vandermonde result to this guy
    #     print(np.linalg.qr(vandermonde_matrix))
    #     qr_factorized= np.linalg.qr(vandermonde_matrix)[0][:,1:]
    #     return qr_factorized

    # def linear_regression(self,qr_factorized):
    #     #run the whole iterative loop
    #     #return self.input_data.LinearRegression.fit()
    #     old_data = self.input_data
    #     baseline = []
    #     predicted_data = []
        

    #     for i in range(self.loops):
    #         predicted_data = LinearRegression.fit(qr_factorized,old_data).predict(qr_factorized)
    #         old_data = np.data(np.minimum(self.input_data,predicted_data))
    #     baseline = old_data
    #     return baseline
                    


#_____________________________________________________________________


# #def (readfile) - to go into the ABC 
# class BaselineRemoval():   

#     def __init__(self,input_data):

#         self.input_data = np.array(input_data)
#         self.vander_degree  = 2
#         #self.error = 0.001
#         self.loops = 100

#     def vandermonde(self): 
        
#         vandermonde_matrix=[]
#         #make a list from 1 to N of the total # of entries in the dataset
#         length_data = list(range(1,len(self.input_data)))
#         for i in range(self.vander_degree+1): #why is it plus 1
#             temp = length_data**i
#             vandermonde_matrix=np.hstack([vandermonde_matrix,temp]) #
#             print(vandermonde_matrix)
#         return vandermonde_matrix

#         #X = np.transpose(np.vstack((input_array_for_poly**k for k in range(degree_for_poly+1)))) 
#         #count the total entries in df  our data and then use that to create an N number of values in our vandermonde



#         #currently just returning the exact section that we want, after creating our vandermonde array
#     def qr_factorization(vandermonde_matrix):
#         #need to pass my vandermonde result to this guy
#         print(np.linalg.qr(vandermonde_matrix))
#         qr_factorized= np.linalg.qr(vandermonde_matrix)[0][:,1:]
#         return qr_factorized

#     def linear_regression(self,qr_factorized):
#         #run the whole iterative loop
#         #return self.input_data.LinearRegression.fit()
#         old_data = self.input_data
#         baseline = []
#         predicted_data = []
        

#         for i in range(self.loops):
#             predicted_data = LinearRegression.fit(qr_factorized,old_data).predict(qr_factorized)
#             old_data = np.data(np.minimum(self.input_data,predicted_data))
#         baseline = old_data
#         return baseline
                    
# if __name__=="__main__":
#         input_data = [1,2,5,62,24,663,33,45,35,134,1,123,42]
#         object = BaselineRemoval(input_data)
#         vandermonde_matrix = object.vandermonde(input_data)
#         qr_factorized = vandermonde_matrix.qr_factorization(vandermonde_matrix)
#         baseline = BaselineRemoval.linear_regression(qr_factorized)
#         print(baseline)

#________________________________________________________________

    #remove the input data since i already passed it in init and im passing init through self

        

#     #describe the process of using a vandermonde matrix to perform a linear regression by fitting our data to the qr factorization of a vandermonde matrix


# #def (readfile) - to go into the ABC 
# class BaselineRemoval():   

#     def __init__(self,input_data):

#         self.input_data = np.array(input_data)
#         self.vander_degree  = 2
#         #self.error = 0.001
#         self.loops = 100

#     def vandermonde(self): 
        
#         vandermonde_matrix=[]
#         #make a list from 1 to N of the total # of entries in the dataset
#         length_data = list(range(1,len(self.input_data)))
#         for i in range(self.vander_degree+1): #why is it plus 1
#             temp = length_data**i
#             vandermonde_matrix=np.hstack([vandermonde_matrix,temp]) #
#             print(vandermonde_matrix)
#         return np.transpose(vandermonde_matrix)

#         #X = np.transpose(np.vstack((input_array_for_poly**k for k in range(degree_for_poly+1)))) 
#         #count the total entries in df  our data and then use that to create an N number of values in our vandermonde



#         #currently just returning the exact section that we want, after creating our vandermonde array
#     def qr_factorization(self,vandermonde_matrix):
#         #need to pass my vandermonde result to this guy
#         print(np.linalg.qr(vandermonde_matrix))
#         return np.linalg.qr(vandermonde_matrix)[0][:,1:]

#     def linear_regression(self,vandermonde_matrix):
#         #run the whole iterative loop
#         #return self.input_data.LinearRegression.fit()
#         old_data = self.input_data
#         baseline = []
#         predicted_data = []
        

#         for i in range(self.loops):
#             predicted_data = LinearRegression.fit(vandermonde_matrix,old_data).predict(vandermonde_matrix)
#             old_data = np.data(np.minimum(self.input_data,predicted_data))
#         baseline = old_data
#         return baseline
#                     #currently not checking the error (criteria>=gradient) and (nrep<=repitition):
#             #ypred=self.lin.fit(polx,yold).predict(polx)
            

#             #ywork=np.array(np.minimum(yorig,ypred))
#             #criteria=sum(np.abs((ywork-yold)/yold))
#             #yold=ywork
#             #nrep+=1
#         #corrected=yorig-ypred
#         #corrected=np.array(list(corrected))
#         #return 0

        
#     def baseline_removal(self): #and anything else I need to do the final computation which is removing the baseline from input_array
#         vandermonde_matrix = vandermonde(self)
#         qr_factorized = qr_factorization(self, vandermonde_matrix)
#         baseline = linear_regression(self,qr_factorized)
#         return baseline

# if __name__=="__main__":
#         input_data = [1,2,5,62,24,663]
#         instantiate = BaselineRemoval(input_data)
#         baseline = instantiate.baseline_removal
#         print(baseline)



#     #remove the input data since i already passed it in init and im passing init through self

        

#     #describe the process of using a vandermonde matrix to perform a linear regression by fitting our data to the qr factorization of a vandermonde matrix





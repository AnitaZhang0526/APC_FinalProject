import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
#from scipy.sparse import csc_matrix, eye, diags
#from scipy.sparse.linalg import spsolve
#import warnings
#warnings.filterwarnings('ignore')


#def (readfile) - to go into the ABC 

#parse out the math that i dont understand as methods here: 
    
    def __init__(self,input_data):

        self.input_data = np.array(input_data)
        self.vander_degree  = 2
        self.error = 0.001
        self.loops = 100

    def linear_regression(self):
        #run the whole iterative loop
        #return self.input_data.LinearRegression.fit()

        polx=self.poly(list(range(1,len(yorig)+1)),degree)
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


    def baseline_removal(self): #probably the output from the linear_regression file 
        return null

    def vandermonde(self): 
        return np.linalg.qr(X)[0][:,1:]

    #X = np.transpose(np.vstack((input_array_for_poly**k for k in range(degree_for_poly+1)))) 
    #count the total entries in our data and then use that to create an N number of values in our vandermonde



    #currently just returning the exact section that we want, after creating our vandermonde array
    def qr_factorization(self):
        return self.np.linalg.qr(X)[0][:,1:]

    def baseline_removal(self): #and anything else I need to do the final computation which is removing the baseline from input_array
        return thingwithnobaseline



    #remove the input data since i already passed it in init and im passing init through self

        

    #describe the process of using a vandermonde matrix to perform a linear regression by fitting our data to the qr factorization of a vandermonde matrix




#____________________________________________________________________________________fuck ya

        

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
        


#def (readfile) - to go into the ABC 

class BaselineRemoval():
    '''input_array: A pandas dataframe column provided in input as dataframe['input_df_column']. It can also be a Python list object
    degree: Polynomial degree
    '''     
    def __init__(self,input_array):
        self.input_array=input_array
        self.lin=LinearRegression()

    def poly(self,input_array_for_poly,degree_for_poly):
        '''qr factorization of a matrix. q` is orthonormal and `r` is upper-triangular.
        - QR decomposition is equivalent to Gram Schmidt orthogonalization, which builds a sequence of orthogonal polynomials that approximate your function with minimal least-squares error
        - in the next step, discard the first column from above matrix.
        - for each value in the range of polynomial, starting from index 0 of pollynomial range, (for k in range(p+1))
            create an array in such a way that elements of array are (original_individual_value)^polynomial_index (x**k)
        - concatenate all of these arrays created through loop, as a master array. This is done through (np.vstack)
        - transpose the master array, so that its more like a tabular form(np.transpose)'''
        print('input array is',input_array_for_poly)
        input_array_for_poly = np.array(input_array_for_poly)
        print('input post random line array is',input_array_for_poly)
        X = np.transpose(np.vstack((input_array_for_poly**k for k in range(degree_for_poly+1))))  #here we are adding a row, but the power is ^0 for the first set so we just get 1's 
        #need to figure out why the 'degree' matters here, so like then i could probably compute this array instead in a dumb way' 
        print('final form x',X)
        
        #maybe i should manually compute QR value here so that i can show some math
        
        print('the linalg version',np.linalg.qr(X)[0][:,1:]) #this is extracting just Q but without the first column for some reason, probs because first row of our matrix was 1's
        return np.linalg.qr(X)[0][:,1:]

    def ModPoly(self,degree=2,repitition=100,gradient=0.001):
        '''Implementation of Modified polyfit method from paper: Automated Method for Subtraction of Fluorescence from Biological Raman Spectra, by Lieber & Mahadevan-Jansen (2003)
        
        degree: Polynomial degree, default is 2
        repitition: How many iterations to run. Default is 100
        gradient: Gradient for polynomial loss, default is 0.001. It measures incremental gain over each iteration. If gain in any iteration is less than this, further improvement will stop
        '''

        #initial improvement criteria is set as positive infinity, to be replaced later on with actual value
        criteria=np.inf

        baseline=[]
        corrected=[]

        ywork=self.input_array
        yold=self.input_array
        yorig=self.input_array

        polx=self.poly(list(range(1,len(yorig)+1)),degree)
        print('list range is',list(range(1,len(yorig)+1)) )
        print('range is',(range(1,len(yorig)+1)) )
        print('polx is',polx)

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
        

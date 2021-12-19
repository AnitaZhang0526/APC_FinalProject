#required libraries are as follows: 
import csv
import os
import pandas as pd
from Code.peak import Peak

"""
BaselineRemoval method takes an array of input data and returns the data with the baseline removed. 
BaselineRemoval uses an Ordinary Linear Regression method that fits to the QR-factorized Vandermonde matrix
This method is based on the process outlined in "Automated Method for Subtraction of Fluorescence from Biological Raman Spectra" by Lieber et al, 2003
This script was based on the implementation available at: https://github.com/StatguyUser/BaselineRemoval
"""

def load_peaks(filename):
    """
    :param filename: name of csv data file
    :type filename: string
    :return: a dataFrame containing the FWHM, center, intensity, and type of peaks
    """
    d = os.path.dirname(os.path.realpath(__file__))
    input_path = os.path.join(d, 'Input', str(filename)) # get the full path of the file
    peaks_df = pd.read_csv(input_path, skiprows=1, header=None, names=['FWHM','center','intensity','type']) # read file and store in dataFrame
    
    peaks = []
    for idx, row in peaks_df.iterrows():
        peak = Peak(row.FWHM,row.center,row.intensity,row.type) # store into peak object
        peaks.append(peak)
    
    return peaks
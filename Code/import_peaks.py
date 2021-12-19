#required libraries are as follows: 
import csv
import os
import pandas as pd
from Code.peak import Peak

"""
LoadPeaks method takes a CSV input file of peaks and returns a list of peak objects. 
This will be useful in using the compare-to-database code in isolation if the user has their own peak data to import and use.
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
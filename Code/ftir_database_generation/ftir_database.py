# peaks_ftir_database.py
# 
# This script obtains the peaks from the ftir_library.csv
# and ftir_metadata.csv. The information of the sample (name, source, 
# spectral resolution, etc.) corresponding to sample id has been
# presented in the "ftir_metadata.csv". The wavenumber and intensity to 
# correspoding sample id are saved in "ftir_library.csv". This codes  
# produces a file "ftir_peaks.csv" that has peak intensities with sample id 
# and sample name.   

# importing the required packages 
from collections import _OrderedDictItemsView, Counter
from numpy.core.fromnumeric import size
import pandas as pd
import numpy as np
from numpy import asarray
from numpy import savetxt
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
 
# Creating Panda Dataframe from .csv files  
data_metadata = pd.read_csv("./Code/databases/ftir_metadata.csv")
data_library = pd.read_csv("./Code/databases/ftir_library.csv")

# Saving sample parameters as dataframe arrays 
sample_wavenumber = data_library.wavenumber 
sample_intensity = data_library.intensity
sample_id = data_library.sample_name
sample_name = data_metadata.spectrum_identity
sample_source = data_metadata.organization 

# Counter setup to take the repetition of sample id into account. 
# The counter "count" will be used to count the number of datapoints for 
# each material in the database. "rep_cum" is used to have cumulative 
# data points. 
count = Counter(sample_id)
rep = list(count.values())
rep_cum = np.cumsum(rep)

# Converting database as numpy array.
id = np.array(list(sample_id))
intensity = np.array(list(sample_intensity))
wavenumber = np.array(list(sample_wavenumber))
name = np.array(list(sample_name))
name_mod = np.append(name, "None") 

# Splitting the single arrays into multiple arrays
# corresponding to datapoints of each material   
id_split = np.split(id,rep_cum)
intensity_split = np.split(intensity,rep_cum)
wavenumber_split = np.split(wavenumber,rep_cum)  

# Calculating the peaks intensity and the corresponding wavenumber. 
# The three most intense peaks have been considered for the comparison.    
length_intensity = len(intensity_split) - 1
cutoff_intensity = None
num_peaks = 3
output1 = []
output2 = []
length = []  

for j in range(length_intensity):
    x = intensity_split[j]
    peaks, _ = find_peaks(x, height = cutoff_intensity)
    sort_indices = np.argsort(x[peaks])
    sort_peaks = np.flip(np.array(peaks)[sort_indices])
    new_peaks = sort_peaks[:num_peaks]
    length_peaks = len(new_peaks) 
    wavenumber_peaks = np.empty(length_peaks)
    intensity_peaks = np.empty(length_peaks)
    for i in range(length_peaks):
        wavenumber_peaks[i] = wavenumber_split[j][new_peaks[i]]
        intensity_peaks[i] = intensity_split[j][new_peaks[i]]
    output1.append(wavenumber_peaks)
    output2.append(intensity_peaks)


# Here the final peaks corresponding to sample id, name and, resources 
# have been saved in the ftir_peaks.csv  
df1 = pd.DataFrame(output1)
df2 = pd.DataFrame(output2)
df = pd.concat([df1, df2], axis=1)

df.insert(0, "Sample Name", sample_name, True)
df.insert(1, "Source", sample_source, True)

# Removing the duplicate peaks coming from different sources for same material
df = df.drop_duplicates()

# adding column name to the respective columns
df.columns =['name', 'organization/article', 'wavenumber_1', 'wavenumber_2', 'wavenumber_3', 'intensity_1', 'intensity_2', 'intensity_3']'

# Saving the dataframe containing the peak information as .csv file
df.to_csv('./Code/databases/ftir_peaks.csv', index = False)


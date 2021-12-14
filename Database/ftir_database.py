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
data_metadata = pd.read_csv("ftir_metadata.csv")
data_library = pd.read_csv("ftir_library.csv")

# Saving sample parameters as arrays
sample_wavenumber = data_library.wavenumber 
sample_intensity = data_library.intensity
sample_id = data_library.sample_name
sample_name = data_metadata.spectrum_identity
sample_source = data_metadata.organization 

# Counter setup to take the repetition of sample id into account
count2 = Counter(sample_id)
rep = list(count2.values())
rep_cum = np.cumsum(rep)

# Converting database as numpy array
id = np.array(list(sample_id))
intensity = np.array(list(sample_intensity))
wavenumber = np.array(list(sample_wavenumber))
name = np.array(list(sample_name))
name_mod = np.append(name, "None") 

# Splitting the arrays 
id_split = np.split(id,rep_cum)
intensity_split = np.split(intensity,rep_cum)
wavenumber_split = np.split(wavenumber,rep_cum)  

# Calculating the peaks wavenumber and intensity
length_intensity = len(intensity_split)-1

output = []
length = []  
for j in range(length_intensity):
    x = intensity_split[j]
    peaks, _ = find_peaks(x, height=0.5)
    length_peaks = len(peaks) 
    wavenumber_peaks = np.empty(length_peaks)
    for i in range(length_peaks):
        wavenumber_peaks[i] = wavenumber_split[j][peaks[i]]
    output.append(wavenumber_peaks)

df = pd.DataFrame(output)
print(sample_name)
df.insert(0, "Sample Name", sample_name, True)
df.insert(1, "Source", sample_source, True)
df.to_csv('ftir_peaks.csv', index = False)



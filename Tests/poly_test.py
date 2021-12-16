from Code.poly import Poly
import numpy as np
import pandas as pd
from Code.strategy import Strategy

# reading in test file
f = open('Malli_80s.allASC.ASC', 'r')
data = np.genfromtxt(f, delimiter=' ')
x = data[:,0]
I = data[:,1]
I = I/max(I)
spectrum = pd.DataFrame({'x':x, 'y':I})

# test that peak finding works (tests accuracy of peak locations,
# widths, and intensities)
def test_get_peak_params():
    
    poly_input = Poly(spectrum) 
    
    # true values
    true_width     = 2.011781083433397
    true_center    = 5.473570731463108
    true_intensity = 0.08334675892834108
    
    # check that calculated values of 21st peak match known true values
    test_peak = poly_input.get_peaks_params()[21]
    assert(test_peak.FWHM == true_width)
    assert(test_peak.center == true_center)
    assert(test_peak.intensity == true_intensity)
    
def test_get_peak_params_edge():
    x1 = np.linspace(0,90,9000)
    y1 = [1]*len(x1)
    spectrum1 = {'x':x1,'y':y1}
    poly_input = Poly(spectrum1) 
    
    # check that calculated values of 21st peak match known true values
    peaks = poly_input.get_peaks_params()
    print(len(peaks))
    assert(len(peaks)==0)
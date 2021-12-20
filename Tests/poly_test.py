from Code.poly import Poly
import numpy as np
import pandas as pd
from Code.strategy import Strategy

# reading in test file
spectrum = pd.read_csv('Code/Input/1-1-4-11_pH0_3-17-2020.csv', skiprows=2, header=None, names=['x','y'])
spectrum['y'] = spectrum['y']/max(spectrum['y'])

# test that peak finding works (tests accuracy of peak locations,
# widths, and intensities)
def test_get_peak_params():
    
    poly_input = Poly(spectrum) 
    
    # true values
    true_width     = 413.01089140220415
    true_center    = 1052.3381085335463
    true_intensity = 0.16871946980663696
    
    # check that calculated values of 21st peak match known true values
    test_peak = poly_input.get_peaks_params()[6]
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
    assert(len(peaks)==1)
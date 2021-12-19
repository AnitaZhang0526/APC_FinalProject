import pytest
from src.peak_profile_fitting_factory import PeakProfileFitting_Factory as PPF_factory
from src.rietveld import Rietveld
from src.poly import Poly
import numpy as np
from src.strategy import Strategy
import pandas as pd

# f = open('Malli_80s.allASC.ASC', 'r')
# data = np.genfromtxt(f, delimiter=' ')
# x = data[:,0]
# I = data[:,1]
# I = I/max(I)
# spectrum = pd.DataFrame({'x':x,'y':I})

spectrum = pd.read_csv('src/input/Malli_80s.csv', skiprows=2, header=None, names=['x','y'])
spectrum['y'] = spectrum['y']/max(spectrum['y'])

def test_poly_factory():
    method = 'Rietveld'
    strategy_choice = 'fast'
    peak_widths = np.arange(5,15)
    cutoff = 0.9
    strategy = Strategy()
    threshold = 0.2
    peaks, r = PPF_factory.factory_method(method, strategy_choice, cutoff, peak_widths, spectrum, strategy, threshold)
    assert(isinstance(r,Rietveld))
    
def test_Rietveld_facotry():
    method = 'polyfit'
    strategy_choice = 'fast'
    peak_widths = np.arange(5,15)
    cutoff = 0.9
    strategy = Strategy()
    threshold = 0.2
    peaks, p = PPF_factory.factory_method(method, strategy_choice, cutoff, peak_widths, spectrum, strategy, threshold)
    assert(isinstance(p,Poly))
    
def test_error_type():
    method = 'hello'
    strategy_choice = 'fast'
    peak_widths = np.arange(5,15)
    cutoff = 0.9
    strategy = Strategy()
    threshold = 0.2
    with pytest.raises(ValueError):
        PPF_factory.factory_method(method, strategy_choice, cutoff, peak_widths, spectrum, strategy, threshold)
    
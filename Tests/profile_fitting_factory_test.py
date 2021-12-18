import pytest
from Code.peak_profile_fitting_factory import PeakProfileFitting_Factory as PPF_factory
from Code.rietveld import Rietveld
from Code.poly import Poly
import numpy as np
from Code.strategy import Strategy
import pandas as pd

f = open('Malli_80s.allASC.ASC', 'r')
data = np.genfromtxt(f, delimiter=' ')
x = data[:,0]
I = data[:,1]
I = I/max(I)
spectrum = pd.DataFrame({'x':x,'y':I})

def test_poly_factory():
    method = 'Rietveld'
    strategy_choice = 'fast'
    peak_widths = np.arange(5,15)
    cutoff = 0.9
    strategy = Strategy()
    threshold = 0.2
    r = PPF_factory.factory_method(method, strategy_choice, cutoff, peak_widths, spectrum, strategy, threshold)
    assert(isinstance(r,Rietveld))
    
def test_Rietveld_facotry():
    method = 'polyfit'
    strategy_choice = 'fast'
    peak_widths = np.arange(5,15)
    cutoff = 0.9
    strategy = Strategy()
    threshold = 0.2
    p = PPF_factory.factory_method(method, strategy_choice, cutoff, peak_widths, spectrum, strategy, threshold)
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
    
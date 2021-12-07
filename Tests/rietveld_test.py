from unittest import mock
from Code.rietveld import Rietveld
import numpy as np
import pandas as pd

f = open('Malli_80s.allASC.ASC', 'r')
data = np.genfromtxt(f, delimiter=' ')
x = data[:,0]
I = data[:,1]
spectrum = pd.DataFrame({'x':x,'y':I})
I = I/max(I)

def test_constructor():
    peak_widths = np.arange(5,15)
    cutoff = 0.9
    a = Rietveld(cutoff,peak_widths,spectrum)
    assert(a.x==x)
    assert(a.y==I)

def test_get_peaks():
    first_peak_idx = 11
    peak_widths = np.arange(5,15)
    cutoff = 0.9
    rietveld_input = Rietveld(cutoff,peak_widths,spectrum)
    peaks_found = rietveld_input.get_peaks()
    assert(peaks_found[0]==first_peak_idx)
    
def test_make_spec():
    peak_widths = np.arange(5,15)
    cutoff = 0.9
    rietveld_input = Rietveld(cutoff,peak_widths,spectrum)
    peak_indices = rietveld_input.get_peaks()
    L = peak_indices.shape[0]
    model_choices = []
    for i in range(L):
        model_choices.append('GaussianModel')
    spec = rietveld_input.make_spec(model_choices)
    assert(spec['modelType'].shape[0]==len(peak_indices))
    
def test_make_one_model():
    rietveld_input = Rietveld(cutoff,peak_widths,spectrum)
    peak_widths = np.arange(5,15)
    cutoff = 0.9
    peak_indices = rietveld_input.get_peaks()
    L = peak_indices.shape[0]
    model_choices = []
    for i in range(L):
        model_choices.append('GaussianModel')
    spec = rietveld_input.make_spec(model_choices)
    composite_model, params = rietveld_input.make_one_model(spec)
    assert(len(params)==L*5)

def test_find_best_fit():
    rietveld_input = Rietveld(cutoff,peak_widths,spectrum)
    peak_widths = np.arange(5,15)
    cutoff = 0.9
    best_model_choices, best_values = rietveld_input.find_best_fit()
    assert(len(best_model_choices)==10)
    assert(isinstance(best_values,dict))

@mock.patch.object(Rietveld,'find_best_fit')
def test_get_params(mock):
    rietveld_input = Rietveld(x,I)
    best_model_choices = ['GaussianModel']*10
    best_values = {'m0_amplitude': 1.0291383664365865,
                   'm0_center': 1.00835563344582,
                   'm0_sigma': 1.1287801933468649,
                   'm1_amplitude': 0.19175865755593524,
                   'm1_center': 7.249916482746309,
                   'm1_sigma': 0.0905743862326664,
                   'm2_amplitude': 0.06880728843927042,
                   'm2_center': 12.576311604803152,
                   'm2_sigma': 0.056336821657227566,
                   'm3_amplitude': 13.420738614064426,
                   'm3_center': 20.53249711767651,
                   'm3_sigma': 44.19726100039618,
                   'm4_amplitude': 0.08651833834136713,
                   'm4_center': 21.864303967336863,
                   'm4_sigma': 0.078203048847664,
                   'm5_amplitude': 0.025048579947275607,
                   'm5_center': 21.775543551229923,
                   'm5_sigma': 0.15313426386971732,
                   'm6_amplitude': 0.21626620768052274,
                   'm6_center': 27.37113321048403,
                   'm6_sigma': 0.1290768365583021,
                   'm7_amplitude': 0.07716633811702212,
                   'm7_center': 29.401631437879672,
                   'm7_sigma': 0.06844054126031233,
                   'm8_amplitude': 0.26002862127163795,
                   'm8_center': 30.222872708227133,
                   'm8_sigma': 0.16101878637459102,
                   'm9_amplitude': 0.1606060078236745,
                   'm9_center': 34.48205912997776,
                   'm9_sigma': 0.10500064381692818}
    cutoff = 0.9
    peak_widths = np.arange(5,15)
    mock.return_value = [best_model_choices, best_values]
    FWHM,center,intensity = rietveld_input.get_params()
    assert(len(FWHM)==10)
    assert(len(center)==10)
    assert(len(intensity)==10)

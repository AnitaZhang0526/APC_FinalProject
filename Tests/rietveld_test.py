from unittest import mock
from Code.rietveld import Rietveld
import numpy as np
import pandas as pd
from Code.strategy import Strategy

f = open('Malli_80s.allASC.ASC', 'r')
data = np.genfromtxt(f, delimiter=' ')
x = data[:,0]
I = data[:,1]
I = I/max(I)
spectrum = pd.DataFrame({'x':x,'y':I})

def test_constructor():
    peak_widths = np.arange(5,15)
    strategy = Strategy()
    cutoff = 0.9
    rietveld_input = Rietveld(cutoff,peak_widths,spectrum,strategy)
    assert((rietveld_input.x==x).all())
    assert((rietveld_input.I==I).all())

def test_get_peaks():
    strategy = Strategy()
    first_peak_idx = 11
    peak_widths = np.arange(5,15)
    threshold = 0.2
    cutoff = 0.9
    rietveld_input = Rietveld(cutoff,peak_widths,spectrum,strategy)
    peaks_found = rietveld_input.get_peaks(threshold)
    assert(peaks_found[0]==first_peak_idx)
    
def test_make_one_model():
    strategy = Strategy()
    cutoff = 0.9
    peak_widths = np.arange(5,15)
    rietveld_input = Rietveld(cutoff,peak_widths,spectrum,strategy)
    threshold = 0.2
    peak_indices = rietveld_input.get_peaks(threshold)
    L = peak_indices.shape[0]+1
    model_choices = []
    for i in range(L):
        model_choices.append('GaussianModel')
    strategy = Strategy()
    spec = strategy.make_one_spec(model_choices,peak_indices,rietveld_input.I,rietveld_input.x,rietveld_input.peak_widths)
    composite_model, params = rietveld_input.make_one_model(spec)
    assert(len(params)==L*5)

def test_find_best_fit():
    strategy = Strategy()
    peak_widths = np.arange(5,15)
    cutoff = 0.9
    rietveld_input = Rietveld(cutoff,peak_widths,spectrum,strategy)
    threshold = 0.2
    best_model_choices, best_values = rietveld_input.find_best_fit('fast',threshold)
    assert(len(best_model_choices)==11)
    assert(isinstance(best_values,dict))
    
@mock.patch.object(Rietveld,'find_best_fit')
def test_get_peaks_params(mock):
    strategy = Strategy()
    cutoff = 0.9
    peak_widths = np.arange(5,15)
    rietveld_input = Rietveld(cutoff,peak_widths,spectrum,strategy)
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
    mock.return_value = [best_model_choices, best_values]
    threshold = 0.2
    peaks = rietveld_input.get_peaks_params('fast',threshold)
    assert(len(peaks)==10)

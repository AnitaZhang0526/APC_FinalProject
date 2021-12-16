import numpy as np
import pandas as pd
from scipy import signal
from lmfit import models
from strategy import Strategy
from peak_profile_fitting import PeakProfileFitting 
from peak import Peak

"""
a subclass of PeakProfileFitting, a way to profile fit
"""
class Rietveld(PeakProfileFitting):  
    """
    : Rietveld inherits from PeakProfileFitting
    : The class has five properties: 
    : x: type double, from PeakProfileFitting
    : I: type double, from PeakProfileFitting
    : cutoff: type double, a cutoff frequency for rough filtering for initial peak approximation
    : peak_widths: type double array, a range that the a peak's width can fall between
    : strategy: Strategy object, an object that contain choices regarding the optimization process 
    : The class requires four input parameters:
    : cutoff, peak_widths, strategy, and
    : spectrum: dataFrame containing x and y values
    """
    def __init__(self,cutoff,peak_widths,spectrum,strategy):
        super().__init__(spectrum)
        self.cutoff = cutoff
        self.peak_widths = peak_widths
        self.strategy = strategy

    """
    : get rough initial peak estimates (without refinement)
    """
    def get_peaks(self):
        b,a = signal.butter(2, self.cutoff, 'low')
        I_filtered = signal.filtfilt(b,a,self.I)
        peak_indicies = signal.find_peaks_cwt(I_filtered, self.peak_widths)
        threshold = 0.20
        idx =(self.I[peak_indicies]>threshold)
        peak_indicies = peak_indicies[idx]
        return peak_indicies

    """
    : calculate the squared error
    """  
    def cost(self,results):
        c = np.sum(np.power(results-self.I, 2))/len(self.x)
        return c

    """
    : spec: dataFrame object, specification for the composite model
    : make a composite model that fits all peaks
    """  
    def make_one_model(self,spec):
        x = self.x
        I = self.I
        x_min = np.min(x)
        x_max = np.max(x)
        x_range = x_max-x_min
        I_max = np.max(I)
        composite_model = None
        params = None

        for i in range(len(spec['modelType'])):
            prefix = f'm{i}_'
            model = getattr(models, spec['modelType'][0])(prefix=prefix)
            model.set_param_hint('sigma', min=1e-6, max=x_range)
            model.set_param_hint('center', min=x_min, max=x_max)
            model.set_param_hint('height', min=1e-6, max=1.1*I_max)
            model.set_param_hint('amplitude', min=1e-6)
            default_params = {
                prefix+'center':spec['center'][i],
                prefix+'height':spec['height'][i],
                prefix+'sigma':spec['sigma'][i]
                }
            model_params = model.make_params(**default_params)
            if params is None:
                params = model_params
            else:
                params.update(model_params)
            if composite_model is None:
                composite_model = model
            else:
                composite_model = composite_model + model
        return composite_model, params

    """
    : strategy_choice: type string, 'fast','best', or 'random'
    : find the best composite model
    """  
    def find_best_fit(self,strategy_choice):
        peak_indices = self.get_peaks()
        lowest_cost = np.inf
        best_model_choices = []
        best_values = []
        specs,model_choices_list = self.strategy.make_specs(strategy_choice,peak_indices,self.x,self.I,self.peak_widths)
        for spec,model_choices in zip(specs,model_choices_list):
            composite_model,params = self.make_one_model(spec)
            predicted_model = composite_model.fit(self.I, params, x=self.x)
            results = predicted_model.eval(params=params)
            c = self.cost(results)
            if c < lowest_cost:
                lowest_cost = c
                best_model_choices = model_choices
                best_values = predicted_model.best_values
        return best_model_choices, best_values

    """
    : strategy_choice: type string, 'fast','best', or 'random'
    : return the refined peak parameters
    """  
    def get_peaks_params(self,strategy_choice):
        peaks = []
        model_choices, values = self.find_best_fit(strategy_choice)
        for i,type in enumerate(model_choices):
            prefix = f'm{i}_'
            key_amp = prefix+'amplitude'
            key_cen = prefix+'center'
            key_sig = prefix+'sigma'
            intensity = values.get(key_amp)
            center = values.get(key_cen)
            sig = values.get(key_sig)
            if model_choices[0] == 'GaussianModel':
                FWHM = 2*sig*np.log(2)
            elif model_choices[0] == 'LorentzianModel':
                FWHM = 2*sig
            elif model_choices[0] == 'VoigtModel':
                FWHM = 3.6013*sig
            peak = Peak(FWHM,center,intensity,type)
            peaks.append(peak)
        return peaks
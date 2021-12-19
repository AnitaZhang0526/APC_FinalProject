import numpy as np
import pandas as pd
from scipy import signal
from lmfit import models
from src.strategy import Strategy
from src.peak_profile_fitting import PeakProfileFitting 
from src.peak import Peak

class Rietveld(PeakProfileFitting):  
    """
    This class inherits from PeakProfileFitting and implements the Rietveld refinement method

    x: type double, x values of spectrum, from PeakProfileFitting
    I: type double, y values of spectrum, from PeakProfileFitting
    cutoff: type double, given by param cutoff
    peak_widths: type double array, given by param peak_widths
    strategy: Strategy object, given by param strategy
    """
    def __init__(self,cutoff,peak_widths,spectrum,strategy):
        """
        Constructor method
        
        :param cutoff: a cutoff frequency for rough filtering for initial peak approximation
        :type cutoff: double
        :pram peak_widths: a range that the a peak's width can fall between
        :type peak_widths: double array
        :param spectrum: dataFrame containing x and y values
        :type spectrum: dataFrame
        :param strategy: an object that contain choices regarding the optimization process
        :type strategy: Strategy object
        :return: a Rietveld object
        """
        super().__init__(spectrum)
        self.cutoff = cutoff
        self.peak_widths = peak_widths
        self.strategy = strategy

    def get_peaks(self, threshold):
        # get rough initial peak estimates (without refinement)
        b,a = signal.butter(2, self.cutoff, 'low') # create a filter
        I_filtered = signal.filtfilt(b,a,self.I) # roughly filter for more precise peak definition
        peak_indicies = signal.find_peaks_cwt(I_filtered, self.peak_widths) # look for rough peaks@
        idx =(self.I[peak_indicies]>threshold) # only look at peaks above a certain amplitude
        peak_indicies = peak_indicies[idx]
        return peak_indicies

    def cost(self,results):
        # calculate the squared error
        c = np.sum(np.power(results-self.I, 2))/len(self.x) # squared error for composite model
        return c

    def make_one_model(self,spec):
        # spec: dataFrame object, specification for the composite model
        # make a composite model that fits all peaks 
        x = self.x
        I = self.I
        x_min = np.min(x)
        x_max = np.max(x)
        x_range = x_max-x_min
        I_max = np.max(I)
        composite_model = None
        params = None
        for i in range(len(spec['modelType'])): # loop through each model
            prefix = f'm{i}_'
            model = getattr(models, spec['modelType'][i])(prefix=prefix) # create a model object based on model type
            model.set_param_hint('sigma', min=1e-6, max=x_range) # set parameter bounds
            model.set_param_hint('center', min=x_min, max=x_max) 
            model.set_param_hint('height', min=1e-6, max=1.1*I_max) 
            model.set_param_hint('amplitude', min=1e-6)
            default_params = {
                prefix+'center':spec['center'][i],
                prefix+'height':spec['height'][i],
                prefix+'sigma':spec['sigma'][i]
                } # set default parameters
            model_params = model.make_params(**default_params) # create a parameter object
            if params is None:
                params = model_params # if model_params is the first set in the composite model, params gets model_params
            else:
                params.update(model_params) # update params to include model_params for other models in the composite model
            if composite_model is None:
                composite_model = model # add the first component to composite model
            else:
                composite_model = composite_model + model # add more components to the composite model
        return composite_model, params

    def find_best_fit(self,strategy_choice,threshold):
        """
        :param strategy_choice: 'fast','best', or 'random'
        :type strategy_choice: str
        :param threshold: only peaks above threashold intensities will be fitted
        :type threshold: double
        :return: the best composite model
        """  
        peak_indices = self.get_peaks(threshold)
        lowest_cost = np.inf
        best_model_choices = []
        best_values = []
        specs,model_choices_list = self.strategy.make_specs(strategy_choice,peak_indices,self.x,self.I,self.peak_widths) # from strategy
        for spec,model_choices in zip(specs,model_choices_list):
            composite_model,params = self.make_one_model(spec) # make one model based on specification
            predicted_model = composite_model.fit(self.I, params, x=self.x) # optimize the composite model using least-square
            results = predicted_model.eval(params=params) # get values of the best-fit composite model
            c = self.cost(results) # compute error
            if c < lowest_cost: # choose best composite model
                lowest_cost = c
                best_model_choices = model_choices 
                best_values = predicted_model.best_values
        return best_model_choices, best_values


    def get_peaks_params(self,strategy_choice,threshold):
        """
        :param strategy_choice: 'fast','best', or 'random'
        :type strategy_choice: str
        :param threshold: only peaks above threashold intensities will be fitted
        :type threshold: double
        :return: the refined peak parameters as a list of Peak objects
        """  
        peaks = []
        model_choices, values = self.find_best_fit(strategy_choice,threshold)
        for i,type in enumerate(model_choices):
            prefix = f'm{i}_' 
            key_amp = prefix+'amplitude'
            key_cen = prefix+'center'
            key_sig = prefix+'sigma'
            intensity = values.get(key_amp) # get parameters
            center = values.get(key_cen)
            sig = values.get(key_sig)
            if model_choices[0] == 'GaussianModel':
                FWHM = 2*sig*np.log(2) # calculate Full width half max ofr a Gaussian peak
            elif model_choices[0] == 'LorentzianModel':
                FWHM = 2*sig # calculate Full width half max ofr a Lorentzian peak
            elif model_choices[0] == 'VoigtModel':
                FWHM = 3.6013*sig # calculate Full width half max ofr a Voight peak
            peak = Peak(FWHM,center,intensity,type) # store into peak object
            peaks.append(peak)
        return peaks

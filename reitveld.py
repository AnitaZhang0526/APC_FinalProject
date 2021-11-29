import math
import random

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import optimize, signal
from lmfit import models

class Reitveld(PeakProfileFitting):

    # initialize the class
    # the class has two properties, each a float array from input file
    # x is the independent variable, and I is the depedent variable
    def __init__(self, x, I):
        self.x = x
        self.I = I

    def getPeaks(self,cutoff,peak_widths):
        b,a = signal.butter(2, cutoff, 'low')
        I_filtered = signal.filtfilt(b,a,self.I)
        peak_indicies = signal.find_peaks_cwt(I_filtered, peak_widths)
        return peak_indicies

    def cost(self,predicted_model):
        c = np.sum(np.power(predicted_model-self.I, 2)) / len(self.x)
        return c

    def make_spec(self,peak_widths,model_choices,peak_indices):
        modelType = []
        height = []
        sigma = []
        center = []
        x_range = np.max(self.x)-np.min(self.x)
        for model_idx,peak_idx in enumerate(peak_indices):
            modelType.append(model_choices[model_idx])
            height.append(self.I[peak_idx])
            sigma.append(x_range/len(self.x)*np.min(peak_widths)),
            center.append(self.x[peak_idx])
        spec = pd.DataFrame({'modelType':modelType,
                             'height':height,
                             'sigma':sigma,
                             'center':center})
        return spec

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
            model = getattr(models, spec[i,['modelType']])(prefix=prefix)
            model.set_param_hint('sigma', min=1e-6, max=x_range)
            model.set_param_hint('center', min=x_min, max=x_max)
            model.set_param_hint('height', min=1e-6, max=1.1*I_max)
            model.set_param_hint('amplitude', min=1e-6)
            default_params = {
                prefix+'center':x_min+x_range*random.random(),
                prefix+'height':I_max*random.random(),
                prefix+'sigma':x_range*random.random()
                } 
            model_params = model.make_params(**default_params, **spec.get(['center','height','sigma']))
            if params is None:
                params = model_params
            else:
                params.update(model_params)
            if composite_model is None:
                composite_model = model
            else:
                composite_model = composite_model + model
        return composite_model, params

    def find_best_fit(self,peak_widths,peak_indices,n_trials):
        options = ['GaussianModel', 'LorentzianModel', 'VoigtModel']
        lowest_cost = np.inf
        best_model_choices = []
        best_params = []
        for i in range(n_trials):
            model_choices = random.choices(options, k=len(peak_indices))
            spec = self.make_spec(self,peak_widths,model_choices,peak_indices)
            composite_model,params = self.make_one_model(spec)
            predicted_model = composite_model.fit(self.I, params, x=self.x)
            c = self.cost(self,predicted_model)
            if c < lowest_cost:
                c = lowest_cost
                best_params = params
                best_model_choices = model_choices
        return best_model_choices, best_params

    def get_params(self,params,model_choices):
        L = len(params)
        FWHM = []
        center = []
        intensity = []
        for one_set,model_choice in zip(params,model_choices):
            c,h,s = one_set
            center.append(c)
            intensity.append(h)
            if model_choice == 'GaussianModel':
                FWHM.append(2*s*np.log(2))
            elif model_choice == 'LorentzianModel':
                FWHM.append(2*s)
            elif model_choice == 'VoightModel':
                FWHM.append(3.6013*s)
        return FWHM,center,intensity

#     def find_best_fit(self,range,initial_guess,peak_indicies,idx):
#        x = self.x
#        x_ref = self.x_ref
#        width = self.width
#        I_peak = peak_indicies[idx]
#        
#        best_params = optimize.minimize(self.cost(x, x_ref, width, I_peak), initial_guess)
#        return best_params

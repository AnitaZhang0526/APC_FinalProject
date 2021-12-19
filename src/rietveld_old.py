import random
import numpy as np
import pandas as pd
from scipy import signal
from lmfit import models

class Rietveld_old():  

    def __init__(self,x,I):
        self.x = x
        self.I = I

    def get_peaks(self,cutoff,peak_widths):
        b,a = signal.butter(2, cutoff, 'low')
        I_filtered = signal.filtfilt(b,a,self.I)
        peak_indicies = signal.find_peaks_cwt(I_filtered,peak_widths)
        threshold = 0.20
        idx =(self.I[peak_indicies]>threshold)
        peak_indicies = peak_indicies[idx]
        return peak_indicies

    def cost(self,results):
        c = np.sum(np.power(results-self.I, 2))/len(self.x)
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
    
    def find_best_fit(self,peak_widths,peak_indices):
        n_trials = 10
        options = ['GaussianModel', 'LorentzianModel', 'VoigtModel']
        lowest_cost = np.inf
        best_model_choices = []
        best_params = []
        for i in range(n_trials):
            model_choices = random.choices(options, k=len(peak_indices))
            spec = self.make_spec(peak_widths,model_choices,peak_indices)
            composite_model,params = self.make_one_model(spec)
            predicted_model = composite_model.fit(self.I, params, x=self.x)
            results = predicted_model.eval(params=params)
            c = self.cost(results)
            if c < lowest_cost:
                c = lowest_cost
                best_params = params
                best_model_choices = model_choices
        return best_model_choices, best_params

    def get_peaks_params(self,params,model_choices):
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
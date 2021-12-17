import numpy as np
from itertools import combinations_with_replacement
import pandas as pd
import random
from scipy import signal

class Strategy:

    """
    : build one composite model based on specifications
	: model_choices: list of strings, indicating the types of peak models
	: peak_indices: list of doubles, peak indices of rough peak positions
    : peak_widths: type double array, a range that the a peak's width can fall between 
	"""
    def make_one_spec(self,model_choices,peak_indices,I,x,peak_widths):
        modelType = []
        height = []
        sigma = []
        center = []
        x_range = np.max(x)-np.min(x)
        for model_idx,peak_idx in enumerate(peak_indices):
            modelType.append(model_choices[model_idx])
            height.append(I[peak_idx])
            sigma.append(x_range/len(x)*np.min(peak_widths)),
            center.append(x[peak_idx])
        modelType.append('GaussianModel')
        height.append(np.mean(I))
        sigma.append(x_range/len(x)*np.min(peak_widths))
        center.append(45)
        spec = pd.DataFrame({'modelType':modelType,
                             'height':height,
                             'sigma':sigma,
                             'center':center})
        return spec

    """
    : make a list of specifications based on user's choice of level of optimization
    : also returns the model choices for each specification
    : strategy_choice: type string, 'fast','best', or 'random'
    : peak_indices: list of doubles, peak indices of rough peak positions
    : x: the independent variable data
	: I: the intensity or the dependent variable data
    : peak_widths: type double array, a range that the a peak's width can fall between 
    """
    def make_specs(self,strategy_choice,peak_indices,I,x,peak_widths):
        specs = []
        options = ['GaussianModel','LorentzianModel','VoigtModel']
        l = len(peak_indices)
        model_choices_list = []
        if strategy_choice == 'best':
            
            model_combinations = list(combinations_with_replacement(options,l))
            for model_choices in model_combinations:
                spec = self.make_one_spec(model_choices,peak_indices,I,x,peak_widths)
                specs.append(spec)
                model_choices_list.append(model_choices)
        elif strategy_choice == 'fast':
            n_trials = len(options)
            for i in range(n_trials):
                model_choices = [options[i]]*len(peak_indices)
                spec = self.make_one_spec(model_choices,peak_indices,I,x,peak_widths)
                print(len(spec['modelType']))
                specs.append(spec)
                model_choices_list.append(model_choices)
        elif strategy_choice == 'random':
            n_trials = 10
            for i in range(n_trials):
                model_choices = random.choices(options,l)
                spec = self.make_one_spec(model_choices,peak_indices,I,x,peak_widths)
                specs.append(spec)
                model_choices_list.append(model_choices)
        model_choices_list.append('GaussianModel')
        return specs,model_choices_list


import numpy as np
from itertools import combinations_with_replacement
import pandas as pd
import random

class Strategy:

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
        spec = pd.DataFrame({'modelType':modelType,
                             'height':height,
                             'sigma':sigma,
                             'center':center})
        return spec

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
                specs.append(spec)
                model_choices_list.append(model_choices)
        elif strategy_choice == 'random':
            n_trials = 10
            for i in range(n_trials):
                model_choices = random.choices(options,l)
                spec = self.make_one_spec(model_choices,peak_indices,I,x,peak_widths)
                specs.append(spec)
                model_choices_list.append(model_choices)
        return specs,model_choices_list


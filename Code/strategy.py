import numpy as np
from itertools import combinations_with_replacement
import pandas as pd
import random
from scipy import signal

class Strategy:
    """
    :This class makes a Strategy object
    """
    def make_one_spec(self,model_choices,peak_indices,I,x,peak_widths):
        """
	    :param model_choices: list of strings, indicating the types of peak models
	    :param peak_indices: list of doubles, peak indices of rough peak positions
        :param peak_widths: type double array, a range that the a peak's width can fall between 
        :returns one composite model based on specifications
	    """
        modelType = []
        height = []
        sigma = []
        center = []
        x_range = np.max(x)-np.min(x)
        for model_idx,peak_idx in enumerate(peak_indices): # loop to add each peak
            modelType.append(model_choices[model_idx]) # add model type
            height.append(I[peak_idx]) # add height
            sigma.append(x_range/len(x)*np.min(peak_widths)) # add sigma
            center.append(x[peak_idx]) # at center
        modelType.append('GaussianModel') # add an additional Gaussian peak to capture the overall trend
        height.append(np.mean(I))
        sigma.append(x_range/len(x)*np.min(peak_widths))
        center.append(np.mean(x))
        spec = pd.DataFrame({'modelType':modelType,
                             'height':height,
                             'sigma':sigma,
                             'center':center
                            }) # store in the form of a dataFrame
        return spec

    def make_specs(self,strategy_choice,peak_indices,I,x,peak_widths):
        """
        :param strategy_choice: type string, 'fast','random', or 'best', where
        'fast' builds three composite models each containing one uniform type of peaks,
        'random' builds 10 random composite models each containing a random combination of peak types,
        'best' builds every possible composite model
        :param peak_indices: list of doubles, peak indices of rough peak positions
        :param x: type double array, the independent variable data
	    :param I: type double array, the intensity or the dependent variable data
        :peak_widths: type double array, a range that the a peak's width can fall between 
        :returns a list of specifications based on user's choice of level of optimization 
        and the model choices for each specification
        """
        specs = []
        options = ['GaussianModel','LorentzianModel','VoigtModel']
        l = len(peak_indices)
        model_choices_list = []
        if strategy_choice == 'best': # 'best' means building every possible composite model
            model_combinations = list(combinations_with_replacement(options,l)) # get all possible combinations
            for model_choices in model_combinations:
                model_choices = list(model_choices) # convert to list
                model_choices.append('GaussianModel') # add an additional Gaussian peak
                spec = self.make_one_spec(model_choices,peak_indices,I,x,peak_widths)
                specs.append(spec) # build a list of specs
                model_choices_list.append(model_choices) # build a list of model choices
        elif strategy_choice == 'fast': # 'fast' means building three composite models 
            n_trials = len(options)
            for i in range(n_trials):
                model_choices = [options[i]]*len(peak_indices) # each composite models contains the same type of peaks
                model_choices.append('GaussianModel') # add an additional Gaussian peak
                spec = self.make_one_spec(model_choices,peak_indices,I,x,peak_widths)
                specs.append(spec) # build a list of specs
                model_choices_list.append(model_choices) # build a list of model choices
        elif strategy_choice == 'random':
            n_trials = 10 # try 10 random combinations of peak types
            for i in range(n_trials):
                model_choices = random.choices(options,l) # choose a random combination of peaks
                model_choices.append('GaussianModel') # add an additional Guassian peak
                spec = self.make_one_spec(model_choices,peak_indices,I,x,peak_widths)
                specs.append(spec) # build a list of specs
                model_choices_list.append(model_choices) # build a list of model choices
        else:
            raise ValueError(f'Invalid strategy choice: {strategy_choice}') # raise an error if the choice is not recognized
        return specs,model_choices_list


from Code.strategy import Strategy
import numpy as np
import pandas as pd

def test_make_one_spec():
    peak_indices = [11, 121, 255, 328, 582, 731, 802, 1020, 1104, 1397, 1674]
    strategy = Strategy()
    model_choices = ['GaussianModel']*12
    I = np.random.rand(1800)
    x = np.arange(0,90,0.05)
    peak_widths = np.arange(5,15)
    spec = strategy.make_one_spec(model_choices,peak_indices,I,x,peak_widths)
    assert((spec['modelType'] == model_choices).all())
    assert(len(spec['height']) == 12)

def test_make_specs():
    strategy = Strategy()
    strategy_choice = 'best'
    peak_indices = [11, 121, 255, 328, 582, 731, 802, 1020, 1104, 1397, 1674]
    I = np.random.rand(1800)
    x = np.arange(0,90,0.05)
    peak_widths = np.arange(5,15)
    specs,model_choices_list = strategy.make_specs(strategy_choice,peak_indices,I,x,peak_widths)
    assert(len(specs) == 78)
    assert(len(model_choices_list) == 78)

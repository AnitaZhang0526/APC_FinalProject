from rietveld import Rietveld
from Pawley import Pawley
from LeBail import LeBail

import numpy as np

class PeakProfileFitting_Factory():
    def factory_method(fitting_type, cutoff, peak_widths, input_df):
        if fitting_type == 'Rietveld':
            return Rietveld(cutoff, peak_widths, input_df)
        elif fitting_type == 'Pawley':
            return Pawley()
        elif fitting_type == 'LeBail':
            return LeBail()
        else:
            raise ValueError(f'Cannot make: {fitting_type}')
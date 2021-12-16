from Code.rietveld import Rietveld
from Code.poly import Poly

import numpy as np

class PeakProfileFitting_Factory():
    def factory_method(fitting_type, cutoff, peak_widths, spectrum, strategy):
        if fitting_type == 'Rietveld':
            return Rietveld(cutoff, peak_widths, spectrum, strategy)
        elif fitting_type == 'polyfit':
        	return Poly(spectrum)
        else:
            raise ValueError(f'Cannot make: {fitting_type}')
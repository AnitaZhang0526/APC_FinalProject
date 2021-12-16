from Code.rietveld import Rietveld
from Code.poly import Poly

import numpy as np

class PeakProfileFitting_Factory():
    def factory_method(method, fitting, cutoff, peak_widths, spectrum, strategy):
        if method == 'Rietveld':
            r =  Rietveld(cutoff, peak_widths, spectrum, strategy)
            print("Calculating parameters of peaks. Please wait.")
            peaks = r.get_peaks_params(fitting)
            print("Done.")
            return peaks, r
        elif method == 'polyfit':
        	p = Poly(spectrum)
        	print("Calculating parameters of peaks. Please wait.")
        	peaks = p.get_peaks_params()
        	print("Done.")
        	return peaks, p
        else:
            raise ValueError(f'Cannot make: {method}')
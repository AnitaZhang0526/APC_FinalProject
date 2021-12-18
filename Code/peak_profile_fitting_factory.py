from Code.rietveld import Rietveld
from Code.poly import Poly

import numpy as np

class PeakProfileFitting_Factory():
    """
    :This class makes either a Poly object or a Rietveld object
    """
    def factory_method(method, strategy_choice, cutoff, peak_widths, spectrum, strategy, threshold):
        """
        :param method: type string, 'Rietveld' or 'polyfit'
        :param strategy_choice: type string, 'fast','random', or 'best'
        :param cutoff: type double, a cutoff frequency for rough filtering for initial peak approximation
        :pram peak_widths: type double array, a range that the a peak's width can fall between
        :param spectrum: dataFrame containing x and y values
        :param strategy: Strategy object, an object that contain choices regarding the optimization process 
        :param threshold: type double, only peaks above threashold intensities will be fitted
        """
        if method == 'Rietveld':
            r =  Rietveld(cutoff, peak_widths, spectrum, strategy) # builds a Rietveld object
            print("Calculating parameters of peaks. Please wait.") # display a message during waiting
            peaks = r.get_peaks_params(strategy_choice,threshold) # call the get_peaks_params method
            print("Done.") # display a message when the process is complete
            return peaks, r
        elif method == 'polyfit':
            p = Poly(spectrum) # builds a Poly object
            print("Calculating parameters of peaks. Please wait.") # display a message during waiting
            peaks = p.get_peaks_params() # call the get_peaks_params method
            print("Done.") # display a message when the process is complete
            return peaks, p
        else:
            raise ValueError(f'Cannot make: {method}') # error if the method is not recognized
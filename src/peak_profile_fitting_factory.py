from src.rietveld import Rietveld
from src.poly import Poly

import numpy as np

class PeakProfileFitting_Factory():
    """
    :This class makes either a Poly object or a Rietveld object
    """
    def factory_method(method, strategy_choice, cutoff, peak_widths, spectrum, strategy, threshold):
        """
        :param method: 'Rietveld' or 'polyfit'
        :type method: str
        :param strategy_choice: 'fast','random', or 'best'
        :type strategy_choice: str
        :param cutoff: a cutoff frequency for rough filtering for initial peak approximation
        :type cutoff: double
        :pram peak_widths: a range that the a peak's width can fall between
        :type peak_widths: double array
        :param spectrum: dataFrame containing x and y values
        :type spectrum: dataFrame
        :param strategy: an object that contain choices regarding the optimization process
        :type strategy: Strategy object
        :param threshold: only peaks above threashold intensities will be fitted
        :type threshold: double
        return: either a Poly object or a Rietveld object
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
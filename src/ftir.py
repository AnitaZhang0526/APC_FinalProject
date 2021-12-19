from src.experimental_technique import ExperimentalTechnique
from src.baseline import baseline_removal, vandermonde_matrix,qr_factorization,linear_regression 
import numpy as np

class FTIR(ExperimentalTechnique):
    """
    The FTIR class inherits from the ExperimentalTechnique class.
    
    :return: an FRIT object
    """
    def filter_baseline(self,spectrum):
        """
        :return: FTIR data after the baseline is removed
        """
        spectrum['y'] = baseline_removal(spectrum['y'])
        return spectrum
    
    def flip_input(self,transmittance,spectrum):
        """
        :return: flipped FTIR data if the data are transmittance 
        and the original data if the data are absorbance
        """
        if transmittance == True:
            spectrum['y'] = 2 - np.log(spectrum['y'])
            return spectrum
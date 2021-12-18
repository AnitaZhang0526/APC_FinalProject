from Code.ExperimentalTechnique import ExperimentalTechnique
from Code.baseline import baseline_removal, vandermonde_matrix,qr_factorization,linear_regression 
import numpy as np

class FTIR(ExperimentalTechnique):
    """
    :return: an FRIT object
	"""
    def filter_baseline(self):
        """
        :return: FTIR data after the baseline is removed
        """
        self.spectrum['y'] = baseline_removal(self.spectrum['y'])
        return self
    
    def flip_input(self,transmittance):
        """
        :return: flipped FTIR data if the data are transmittance 
        and the original data if the data are absorbance
        """
        if transmittance == True:
            self.spectrum['y'] = 2 - np.log(self.spectrum['y'])
        return self
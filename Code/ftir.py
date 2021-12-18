from Code.experimental_technique import ExperimentalTechnique
from Code.baseline import baseline_removal, vandermonde_matrix,qr_factorization,linear_regression 
import numpy as np

class FTIR(ExperimentalTechnique):

	def filter_baseline(self,spectrum):
		spectrum['y'] = baseline_removal(spectrum['y'])
		return self

	def flip_input(self,transmittance,spectrum):
		if transmittance == True:
			spectrum['y'] = 2 - np.log(spectrum['y'])
		return self

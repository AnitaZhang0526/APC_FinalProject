from Code.experimental_technique import ExperimentalTechnique
from Code.baseline import baseline_removal, vandermonde_matrix,qr_factorization,linear_regression 
import numpy as np

class FTIR(ExperimentalTechnique):

	def filter_baseline(self):
		self.spectrum['y'] = baseline_removal(self.spectrum['y'])
		return self

	def flip_input(self,a_or_t):
		if a_or_t == True:
			self.spectrum['y'] = 2 - np.log(self.spectrum['y'])
		return self

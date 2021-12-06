import os
import pandas as pd
import numpy as np

class ExperimentalTechnique():
	def __init__(self, spectrum):
		self.spectrum = spectrum

	def load_data(self,filename):
		input_path = os.path.join(dir, 'Input', str(filename))
		spectrum = pd.read_csv(input_path, skiprows=2, header=None, names=['x','y'])
		return spectrum
import os
import pandas as pd
import numpy as np

class ExperimentalTechnique():
	def __init__(self, spectrum):
		self.spectrum = spectrum

	### not useful because you need spectrum to declare ExperimentalTechnique in the first place
	# def load_data(self, dir, filename):
	# 	input_path = os.path.join(dir, 'Input', str(filename))
	# 	spectrum = pd.read_csv(input_path, skiprows=2, header=None, names=['x','y'])
	# 	spectrum['y']=spectrum['y']/max(spectrum['y'])

	# 	return spectrum
import os

import pandas as pd
import numpy as np

from ExperimentalTechnique import ExperimentalTechnique

class XRD(ExperimentalTechnique):
	def load_data(XRD,dir, filename):
		input_path = os.path.join(dir, 'Input', str(filename))
		input_df = pd.read_csv(input_path, skiprows=2, header=None)
		x = input_df.iloc[:,0].values
		I = input_df.iloc[:,1].values
		I = I/max(I)

		return input_df, x, I
		
	def filter_baseline():
		pass

	def get_peak_features():
		pass

	def test(arg):
		print('link works!')
import os

import pandas as pd
import numpy as np

from ExperimentalTechnique import ExperimentalTechnique

class FTIR(ExperimentalTechnique):
	def load_data(dir, filename):
		input_path = os.path.join(dir, 'Input', str(filename))
		input_df = pd.read_csv(input_path, skiprows=2, header=None)

		return input_df

	def filter_baseline():
		pass

	def get_peak_features():
		pass
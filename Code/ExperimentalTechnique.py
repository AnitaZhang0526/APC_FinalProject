import os
import pandas as pd
import numpy as np

class ExperimentalTechnique():
	def __init__(self, spectrum):
		spectrum['y'] = spectrum['y']/max(spectrum['y'])
		self.spectrum = spectrum
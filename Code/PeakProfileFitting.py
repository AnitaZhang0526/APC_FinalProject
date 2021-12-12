import abc

class PeakProfileFitting(metaclass=abc.ABCMeta):
	def __init__(self,spectrum):
		self.x = spectrum['x']
		self.I = spectrum['y']

	def get_peak_params(self):
		pass
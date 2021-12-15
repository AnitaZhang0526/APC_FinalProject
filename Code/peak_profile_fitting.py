import abc
"""
: the parent class for all profile fitting methods
"""
class PeakProfileFitting(metaclass=abc.ABCMeta):
	"""
	: x: the independent variable data
	: I: the intensity or the dependent variable data
	"""
	def __init__(self,spectrum):
		self.x = spectrum['x']
		self.I = spectrum['y']

	"""
	: not implemented, abstract get_peaks_params methods
	"""
	@abc.abstractmethod
	def get_peaks_params(self):
		pass
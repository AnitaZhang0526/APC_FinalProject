import abc
from abc import abstractmethod

class PeakProfileFitting(metaclass=abc.ABCMeta):

	@abstractmethod
	def __init__(self, cutoff,peak_widths,spectrum,strategy):
		self.x = spectrum['x']
		self.I = spectrum['y']

	def get_peak_params(self):
		pass
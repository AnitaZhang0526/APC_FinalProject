import abc

class PeakSearch(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def curve_fitting(self):
		pass
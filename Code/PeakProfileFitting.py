import abc

class PeakProfileFitting(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def fit_one_peak(self):
		pass

	@abc.abstractmethod
	def combine_all_peaks(self):
		pass
import abc

class ExperimentalTechnique(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def load_data(self):
		pass

	@abc.abstractmethod
	def filter_baseline(self):
		pass

	@abc.abstractmethod
	def get_peak_features(self):
		pass
import abc

class PeakProfileFitting(metaclass=abc.ABCMeta):
	"""
	:This class is the parent class for all profile fitting methods
 
	:x: the independent variable data
	:I: the intensity or the dependent variable data
	"""
	def __init__(self,spectrum):
        """
        :Constructor method
        :param spectrum: dataFrame containing x and y values
        """
		self.x = spectrum['x']
		self.I = spectrum['y']

	# not implemented, abstract get_peaks_params methods
	@abc.abstractmethod
	def get_peaks_params(self):
		pass
from Rietveld import Rietveld
from Pawley import Pawley
from LeBail import LeBail

class PeakProfileFitting_Factory():
	def factory_method(fitting_type):
	    if fitting_type == 'rietveld':
	        return Rietveld()
	    elif fitting_type == 'Pawley':
	        return Pawley()
	    elif fitting_type == 'LeBail':
	        return LeBail()
	    else:
	        raise ValueError(f'Cannot make: {fitting_type}')
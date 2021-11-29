from XRD import XRD
from FTIR import FTIR

class ExperimentalTechnique_Factory():
	def factory_method(input_type):
	    if input_type == 'XRD':
	        return XRD()
	    elif input_type == 'FTIR':
	        return FTIR()
	    else:
	        raise ValueError(f'Cannot make: {input_type}')
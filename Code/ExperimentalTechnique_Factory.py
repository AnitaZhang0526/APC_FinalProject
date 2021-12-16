from xrd import XRD
from ftir import FTIR

class ExperimentalTechnique_Factory():
	def factory_method(input_type, spectrum):
	    if input_type == 'XRD':
	        return XRD(spectrum)
	    elif input_type == 'FTIR':
	        return FTIR(spectrum)
	    else:
	        raise ValueError(f'Cannot make: {input_type}')
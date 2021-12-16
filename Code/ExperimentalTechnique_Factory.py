from Code.xrd import XRD
from Code.ftir import FTIR

class ExperimentalTechnique_Factory():
    def factory_method(input_type, spectrum, transmittance):
        if input_type == 'XRD':
            return XRD(spectrum)
        elif input_type == 'FTIR':
            ftir = FTIR(spectrum)
            ftir = FTIR.filter_baseline(ftir)
            ftir = FTIR.flip_input(ftir, transmittance)
            return ftir
        else:
            raise ValueError(f'Cannot make: {input_type}')
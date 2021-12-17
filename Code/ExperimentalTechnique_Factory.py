from Code.xrd import XRD
from Code.ftir import FTIR
import os
import pandas as pd

class ExperimentalTechnique_Factory():
    def factory_method(inputfile, input_type, transmittance):
        dir = os.path.dirname(os.path.realpath(__file__))
        input_path = os.path.join(dir, 'Input', str(inputfile))
        spectrum = pd.read_csv(input_path, skiprows=2, header=None, names=['x','y'])
        spectrum['y']=spectrum['y']/max(spectrum['y'])

        if input_type == 'XRD':
            return spectrum, XRD(spectrum)
        elif input_type == 'FTIR':
            ftir = FTIR(spectrum)
            ftir = FTIR.flip_input(ftir, transmittance)
            ftir = FTIR.filter_baseline(ftir)

            return spectrum, ftir
        else:
            raise ValueError(f'Cannot make: {input_type}')
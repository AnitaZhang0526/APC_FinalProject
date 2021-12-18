from Code.xrd import XRD
from Code.ftir import FTIR
import pandas as pd

class ExperimentalTechnique_Factory():
    """
    :This class makes either an xrd or a ftir object
    """
    def factory_method(inputfile, input_type, transmittance):
        """
        :param filename: name of the data file
        :type filename: str
        :param transmittance: True or False depending on if the data are for absorbance or transmittance
        :type transmittance: bool
        :return: a dataFrame containing x and y values and an ExperimentalTechnique object
        """
        if input_type == 'XRD':
            xrd = XRD() # create an XRD object if the input type is XRD
            spectrum = xrd.load_data(inputfile) # extract data and create spectrum dataFrame using the load_data method in XRD class
            return spectrum, xrd
        elif input_type == 'FTIR':
            ftir = FTIR() # create a FTIR object if the input type is FTIR
            ftir = FTIR.flip_input(ftir, transmittance) # flip data if y axis is transmittance instead of absorbance
            ftir = FTIR.filter_baseline(ftir) # filter baseline
            spectrum = ftir.load_data(inputfile) # extract data and create spectrum dataFrame using the load_data method in FTIR class
            return spectrum, ftir
        else:
            raise ValueError(f'Cannot make: {input_type}') # error if the input type is not recognized
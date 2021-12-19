from src.xrd import XRD
from src.ftir import FTIR

class ExperimentalTechnique_Factory():
    """
    This class makes either an xrd or a ftir object
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
            spectrum = ftir.load_data(inputfile) # extract data and create spectrum dataFrame using the load_data method in FTIR class
            spectrum = ftir.flip_input(transmittance,spectrum) # flip data if y axis is transmittance instead of absorbance
            spectrum = ftir.filter_baseline(spectrum) # filter baseline
            return spectrum, ftir
        else:
            raise ValueError(f'Cannot make: {input_type}') # error if the input type is not recognized
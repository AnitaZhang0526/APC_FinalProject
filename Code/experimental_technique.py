import os
import pandas as pd
import numpy as np


class ExperimentalTechnique():
    """
    This class is the param class for XRD and FTIR
    """
    def load_data(self,filename):
        """
        :param filename: name of csv data file
        :type filename: string
        :return: a dataFrame containing x and y values
        """
        d = os.path.dirname(os.path.realpath(__file__))
        input_path = os.path.join(d, 'Input', str(filename)) # get the full path of the file
        spectrum = pd.read_csv(input_path, skiprows=2, header=None, names=['x','y']) # read file and store in dataFrame
        return spectrum
import pandas as pd
import numpy as np
from scipy.spatial import distance
from Code.peak import Peak

class CompareToDatabase:
    """This class takes in peak information and returns the closest match from the database.
      
    :data_type: type string, given by param data_type
    :peaks: list of Peak objects, given by param peaks
    """

    def __init__(self, data_type = None, peaks = []):
        """
        :Constructor method
        :param data_type: "xrd" or "ftir", defaults to None
        :type data_type:: str
        :param peaks: defaults to an empty list
        :type peaks: list of Peak objects
        :return: a CompareToDatabase object
        """
        self.data_type = data_type
        self.peaks = peaks

    def match(self):
        """
        :return: the closest material match from the XRD or FTIR database, based on data type.
        """
        match = None;

        if self.data_type == "xrd":
            match = self._match_xrd()
        elif self.data_type == "ftir":
            match = self._match_ftir()
        
        return match

    # --------- Private methods ---------

    # Returns match from XRD database
    def _match_xrd(self):
        match = None
        min_distance = float("inf")
        input_peaks = self._xrd_most_intense_peaks(self.peaks)

        # Must input at least 3 peaks to get a match
        if (len(input_peaks) < 3):
            return match

        dtype_dict = {
            "2_theta_1":float,
            "intensity_1":float,
            "2_theta_2":float,
            "intensity_2":float,
            "2_theta_3":float,
            "intensity_3":float,
            "material_name":str,
            "material_formula":str,
        }
        db = pd.read_csv("./Code/databases/xrd.csv", dtype = dtype_dict)

        two_theta_one = db['2_theta_1']
        intensity_one = db['intensity_1']
        two_theta_two = db['2_theta_2']
        intensity_two = db['intensity_2']
        two_theta_three = db['2_theta_3']
        intensity_three = db['intensity_3']
        
        for i in range(len(two_theta_one)):
            db_peaks = [
                Peak(None,two_theta_one[i],intensity_one[i],None),
                Peak(None,two_theta_two[i],intensity_two[i],None),
                Peak(None,two_theta_three[i],intensity_three[i],None),
            ]
            distance = self._xrd_distance(input_peaks, db_peaks)
            if distance < min_distance:
                min_distance = distance
                match = db.iloc[i, :]

        return match

    # Takes all peaks and returns the three most intense
    def _xrd_most_intense_peaks(self, peaks):
        sorted_peaks = sorted(peaks, key = lambda x: x.intensity, reverse = True)
        return sorted_peaks[:3]
    
    # Takes all peaks and returns the three most intense
    def _ftir_most_intense_peaks(self, peaks):
        sorted_peaks = sorted(peaks, key = lambda x: x.center, reverse = True)
        sorted_three_peaks = sorted_peaks[:3]
        sorted_three_peaks.reverse()
        return sorted_three_peaks

    # Calculates euclidean distances between two sets of three peaks
    def _xrd_distance(self, input_peaks, db_peaks):
        i = []
        for ip in input_peaks:
            i.append(ip.center)
            i.append(ip.intensity)

        d = []
        for dp in db_peaks:
            d.append(dp.center)
            d.append(dp.intensity)

        return distance.euclidean(i, d)

       # Calculates euclidean distances between two sets of three peaks
    def _ftir_distance(self, input_peaks, db_peaks):
        i = []
        for ip in input_peaks:
            i.append(ip.center) 
        d = []
        for dp in db_peaks:
            d.append(dp.center)

        return distance.euclidean(i, d)    

       # Return match from FTIR database 
    def _match_ftir(self):
        match = None
        min_distance = float("inf")
        input_peaks = self._ftir_most_intense_peaks(self.peaks)

        # Must input at least 3 peaks to get a match
        if (len(input_peaks) < 3):
            return match

        dtype_dict = {
            
            "wavenumber_1":float, 
            "wavenumber_2":float,
            "wavenumber_3":float,
            "name":str,
            "organization/article":str,
        }
        db = pd.read_csv("./Code/databases/ftir_peaks.csv", dtype = dtype_dict)

        
        wavenumber_one = db['wavenumber_1']        
        wavenumber_two = db['wavenumber_2']
        wavenumber_three = db['wavenumber_3']
        
        for i in range(len(wavenumber_one)):
            db_peaks = [
                Peak(None,wavenumber_one[i],None,None),
                Peak(None,wavenumber_two[i],None,None),
                Peak(None,wavenumber_three[i],None,None),
            ]
            distance = self._ftir_distance(input_peaks, db_peaks)
            if distance < min_distance:
                min_distance = distance
                match = db.iloc[i, :]

        return match


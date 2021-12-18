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
        :param data_type: type string, "xrd" or "ftir", defaults to None
        :param peaks: list of Peak object, defaults to an empty list
        """
        self.data_type = data_type
        self.peaks = peaks

    def match(self):
        """
        :returns the closest material match from the XRD or FTIR
        database, based on data type.

        :return: returns the closest material match
        :rtype: list with attributes in the following order: 
            [2_theta_1, intensity_1, 2_theta_2, intensity_2, 2_theta_3, intensity_3, material_name, material_formula]
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

    # Takes all XRD peaks and returns the three most intense
    def _xrd_most_intense_peaks(self, peaks):
        sorted_peaks = sorted(peaks, key = lambda x: x.intensity, reverse = True)
        return sorted_peaks[:3]

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

    # Returns match from FTIR database
    def _match_ftir(self):
        # TODO this method will be filled in later
        return None
# compare_to_database.py
#
# This class takes in peak information
# and returns the closest match from the database.

import pandas as pd
import numpy as np
from scipy.spatial import distance

class CompareToDatabase:

    # data_type = "xrd" or "ftir"
    # peaks = 2-D array of peak locations (2-theta) and their relative intensities
    #  ex: [[14.24, 90], [38.88, 100], ...]
    def __init__(self, data_type = None, peaks = []):
        self.data_type = data_type
        self.peaks = peaks

    def match(self):
        match = None;

        if self.data_type == "xrd":
            match = self._match_xrd()
        elif self.data_type == "ftir":
            match = self._match_ftir()
        
        return match

    # --------- Private methods ---------

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
                [two_theta_one[i], intensity_one[i]],
                [two_theta_two[i], intensity_two[i]],
                [two_theta_three[i], intensity_three[i]],
            ]
            distance = self._xrd_distance(input_peaks, db_peaks)
            if distance < min_distance:
                min_distance = distance
                match = db.iloc[i, :]

        return match

    def _xrd_most_intense_peaks(self, peaks):
        sorted_peaks = sorted(peaks, key = lambda x: x[1], reverse = True)
        return sorted_peaks[:3]

    def _xrd_distance(self, input_peaks, db_peaks):
        i = np.array(input_peaks).flatten()
        d = np.array(db_peaks).flatten()
        return distance.euclidean(i, d)

    def _match_ftir(self):
        # TODO this method will be filled in later
        return None
# compare_to_database.py
#
# This class takes in peak information
# and returns the closest match from the database.

class CompareToDatabase:

    # data_type = "xrd" or "ftir"
    # peaks = 2-D array of peak locations (2-theta) and their relative intensities
    #  ex: [[14.24, 90], [38.88, 100], ...]
    def __init__(self, data_type = None, peaks = []):
        self.data_type = data_type
        self.peaks = peaks

    def match(self):
        match = None;

        if self.data_type == 'xrd':
            match = self._match_xrd()
        elif self.data_type == 'ftir':
            match = self._match_ftir()
        
        return match

    # --------- Private methods ---------

    def _match_xrd(self):
        return 1

    def _match_ftir(self):
        return 1



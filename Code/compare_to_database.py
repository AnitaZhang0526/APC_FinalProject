# compare_to_database.py
#
# This class takes in peak information
# and returns the closest match from the database.

def CompareToDatabase:

	# data_type = "xrd" or "ftir"
	# peaks = 2-D array of peak locations (2-theta) and their relative intensities
	#  ex: [[14.24, 90], [38.88, 100], ...]
	def __init__(self, data_type, peaks):
    	self.data_type = data_type
    	self.peaks = peaks

    def match():
    	match = None;

    	if data_type == 'xrd':
    		match_xrd()
    	else if data_type == 'ftir':
    		match_ftir()
    	
		return match

	# --------- Private methods ---------

	def _match_xrd():
		return 1

	def _match_ftir():
		return 1



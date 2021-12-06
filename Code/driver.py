# driver for the suite

import argparse
import csv
import os

import pandas as pd
import numpy as np

from ExperimentalTechnique_Factory import ExperimentalTechnique_Factory as ET_Factory
from PeakProfileFitting_Factory import PeakProfileFitting_Factory as PPF_Factory

parser = argparse.ArgumentParser(description='Analyzes results from XRD and FTIR output data.')
parser.add_argument('-d', '--data', type=str, 
	help='Type of data being uploaded, "XRD" or "FTIR".')
parser.add_argument('-a', '--analysis', type=str, 
	help='Type of peak analysis to be performed, "PeakSearch" or "PeakProfileFitting".')
parser.add_argument('-m', '--method', type=str,
	help='Type of PeakProfileFitting algorithm to be used, "Rietveld", "LeBail", or "Pawley".')
parser.add_argument('-i', '--inputfile', type=str,
	help='Filename of input file to be analyzed (e.g. "1-1-4-11_pH0_3-17-2020.csv").')

if __name__ == '__main__':
	args = vars(parser.parse_args())

	if args['data'] and args['analysis'] and args['inputfile']:
		dir = os.path.dirname(os.path.realpath(__file__))

		# input_df = XRD.load_data(dir, args['inputfile']);
		technique = ET_Factory.factory_method(args['data'])
		if (args['analysis'] == 'PeakProfileFitting') and (args['method']):
			analysis = PPF_Factory.factory_method(args['method'])
		input_df = technique.load_data(dir, args['inputfile'])

	else: 
		print('Missing argument.')
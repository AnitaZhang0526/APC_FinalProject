# driver for the suite

import argparse
import csv
import os

import pandas as pd
import numpy as np

parser = argparse.ArgumentParser(description='Analyzes results from XRD and FTIR output data.')
parser.add_argument('-d', '--data', type=str, 
	help='Type of data being uploaded, "XRD" or "FTIR".')
parser.add_argument('-a', '--analysis', type=str, 
	help='Type of peak analysis to be performed, "PeakSearch" or "PeakProfileFitting".')
parser.add_argument('-m', '--method', type=str,
	help='Type of PeakProfileFitting algorithm to be used, "Rietveld", "LeBail", or "Pawley".')

if __name__ == '__main__':
	args = vars(parser.parse_args())

	if args['data'] and args['analysis']:
		dir = os.path.dirname(os.path.realpath(__file__))
		input_path = os.path.join(dir, 'Input', '1-1-4-11_pH0_3-17-2020.csv')

		input_df = pd.read_csv(input_path, skiprows=2, header=None)

		print(args['data'])
		print(args['analysis'])
		print(input_df)
	else: 
		print('Data argument and Analysis argument both required.')
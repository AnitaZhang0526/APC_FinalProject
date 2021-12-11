# driver for the suite

import argparse
import csv
import os

import pandas as pd
import numpy as np

from ExperimentalTechnique_Factory import ExperimentalTechnique_Factory as ET_Factory
from PeakProfileFitting_Factory import PeakProfileFitting_Factory as PPF_Factory

# Test using `python driver.py -d XRD -a PeakProfileFitting -m Rietveld -i 1-1-4-11_pH0_3-17-2020.csv`
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

        technique = ET_Factory.factory_method(args['data'])
        input_df, x, I = technique.load_data(dir,args['inputfile'])
        if (args['analysis'] == 'PeakProfileFitting') and (args['method']):
            cutoff = 0.9
            peak_widths = np.arange(5,15)
            analysis = PPF_Factory.factory_method(args['method'], cutoff, peak_widths, input_df)
            peak_indices = analysis.get_peaks()

            L = peak_indices.shape[0]
            model_choices = []
            for i in range(L):
                model_choices.append('GaussianModel')
            spec = analysis.make_spec(model_choices)
            composite_model, params = analysis.make_one_model(spec)
            best_model_choices, best_values = analysis.find_best_fit()

    else: 
        print('Missing argument.')
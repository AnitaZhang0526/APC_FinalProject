# driver for the suite

import argparse
import csv
import os

import pandas as pd
import numpy as np

from Code.experimental_technique_factory import ExperimentalTechnique_Factory as ET_Factory
from Code.peak_profile_fitting_factory import PeakProfileFitting_Factory as PPF_Factory
from Code.strategy import Strategy
from Code.compare_to_database import CompareToDatabase

"""
This is the driver code that runs the tool suite
from root directory, run by type in:
'python Code/driver.py -d <data_type> -m <method> -f <strategy_choice> -t <True or False> -s <threshold> -i <filename>'
transmittance defaults to True, strategy_choice defaults to "fast", cutoff defaults to "0.9",
range defaults to "5,15", and threshold defaults to "0.2"
e.g. 'python Code/driver.py -d FTIR -m "Rietveld" -f "fast" -t -s -i 1-1-4-11_pH0_3-17-2020.csv'
"""
# parses command line arguments
parser = argparse.ArgumentParser(description='Analyzes results from XRD and FTIR output data.')
parser.add_argument('-d', '--data', type=str, 
    help='Type of data being uploaded, "XRD" or "FTIR".')
parser.add_argument('-t', '--transmittance', dest='transmittance', action='store_true')
parser.add_argument('-m', '--method', type=str,
    help='Type of strategy to be used, "Rietveld" or "polyfit".')
parser.add_argument('-f', '--strategy_choice', type=str,
    help='Type of Rietveld fitting to be used, "best", "fast", or "random".')
parser.add_argument('-c', '--cutoff', type=str,
    help='Cutoff to be used for fitting (e.g. 0.9).')
parser.add_argument('-r', '--range', type=str,
    help='Peak widths range to be used for fitting (e.g. "5,15").')
parser.add_argument('-s', '--threshold', type=str,
    help='Threshold for what counts as a peak (e.g. 0.2).')
parser.add_argument('-i', '--inputfile', type=str,
    help='Filename of input file to be analyzed (e.g. "1-1-4-11_pH0_3-17-2020.csv").')
parser.set_defaults(transmittance=True, strategy_choice="fast", cutoff="0.9", range="5,15", threshold="0.2")

if __name__ == '__main__':
    args = vars(parser.parse_args())

    if args['data'] and args['method'] and args['cutoff'] and args['range'] and args['inputfile']:
        dir = os.path.dirname(os.path.realpath(__file__))

        # (1) Factory methods to create the Experimental Technique and Peak Profile Fitting
        spectrum, technique = ET_Factory.factory_method(args['inputfile'], args['data'], args['transmittance'])
        strategy = Strategy()   

        cutoff = float(args['cutoff']) # convert cutoff to float
        threshold = float(args['threshold'])  # convert threshold to float
        peak_widths_range = args['range'].split(',') # convert peak_widths_range to float
        peak_widths = np.arange(int(peak_widths_range[0]),int(peak_widths_range[1])) # create the full range

        # (2) Calculates the peaks and its parameters from the input data and exports this into a CSV.
        peaks, analysis = PPF_Factory.factory_method(args['method'], args['strategy_choice'], cutoff, peak_widths, spectrum, strategy, threshold)
        
        if not (os.path.isdir(os.path.join(dir, 'Output'))):
            os.mkdir(os.path.join(dir, 'Output')) # create a new file is the file does not already exist
        with open(os.path.join(dir, 'Output', f"peaks_{args['inputfile']}"), 'wt', encoding='UTF-8',newline='') as h:
            csv_peaks = csv.writer(h)
            header_peaks = ['FWHM', 'center', 'intensity', 'type']
            csv_peaks.writerow(header_peaks)
            for each in peaks:     
                entry = [each.FWHM, each.center, each.intensity, each.type]
                csv_peaks.writerow(entry) # write to the peak list file

        # (3) Compares the peak parameters to a database to find a match and exports the result into a CSV.
        print('Comparing peaks to database. Please wait.')
        match = CompareToDatabase(args['data'].lower(), peaks).match()
        print('Done.')
   
        with open(os.path.join(dir, 'Output', f"match_{args['inputfile']}"), 'wt', encoding='UTF-8',newline='') as j:
            csv_match = csv.writer(j)
            header_match = ['2_theta_1', 'intensity_1', '2_theta_2', 'intensity_2', '2_theta_3', 'intensity_3', 'material_name', 'material_formula']
            csv_match.writerow(header_match)
            if not (type(match) == type(None)):     
                csv_match.writerow(match) # write to the match file
            else:
                print("No match determined.")
            
    else: 
        print('Missing argument.')
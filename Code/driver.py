# driver for the suite

import argparse
import csv
import os

import pandas as pd
import numpy as np

from Code.ExperimentalTechnique_Factory import ExperimentalTechnique_Factory as ET_Factory
from Code.PeakProfileFitting_Factory import PeakProfileFitting_Factory as PPF_Factory
from Code.strategy import Strategy
from Code.compare_to_database import CompareToDatabase

# Test from root directory using `python Code/driver.py -d FTIR -m "polyfit" -t -i 1-1-4-11_pH0_3-17-2020.csv`
parser = argparse.ArgumentParser(description='Analyzes results from XRD and FTIR output data.')
parser.add_argument('-d', '--data', type=str, 
    help='Type of data being uploaded, "XRD" or "FTIR".')
parser.add_argument('-t', '--transmittance', dest='transmittance', action='store_true')
parser.add_argument('-m', '--method', type=str,
    help='Type of fitting to be used, "Rietveld" or "polyfit".')
parser.add_argument('-f', '--fitting', type=str,
    help='Type of Rietveld fitting to be used, "best", "fast", or "random".')
parser.add_argument('-c', '--cutoff', type=str,
    help='Cutoff to be used for fitting (e.g. 0.9).')
parser.add_argument('-r', '--range', type=str,
    help='Peak widths range to be used for fitting (e.g. "5,15").')
parser.add_argument('-i', '--inputfile', type=str,
    help='Filename of input file to be analyzed (e.g. "1-1-4-11_pH0_3-17-2020.csv").')
parser.set_defaults(transmittance=True, fitting="best", cutoff="0.9", range="5,15")

if __name__ == '__main__':
    args = vars(parser.parse_args())

    if args['data'] and args['method'] and args['cutoff'] and args['range'] and args['inputfile']:
        dir = os.path.dirname(os.path.realpath(__file__))

        spectrum, technique = ET_Factory.factory_method(args['inputfile'], args['data'], args['transmittance'])
        strategy = Strategy()   

        cutoff = float(args['cutoff'])     
        peak_widths_range = args['range'].split(',')
        peak_widths = np.arange(int(peak_widths_range[0]),int(peak_widths_range[1]))
        peaks, analysis = PPF_Factory.factory_method(args['method'], args['fitting'], cutoff, peak_widths, spectrum, strategy)
        
        if not (os.path.isdir(os.path.join(dir, 'Output'))):
            os.mkdir(os.path.join(dir, 'Output'))
        with open(os.path.join(dir, 'Output', f"peaks_{args['inputfile']}"), 'wt', encoding='UTF-8',newline='') as h:
            csv_peaks = csv.writer(h)
            header_peaks = ['FWHM', 'center', 'intensity', 'type']
            csv_peaks.writerow(header_peaks)
            for each in peaks:     
                entry = [each.FWHM, each.center, each.intensity, each.type]
                csv_peaks.writerow(entry)

        match = CompareToDatabase(args['data'].lower(), peaks).match()
        
        if not (match == None):
            with open(os.path.join(dir, 'Output', f"match_{args['inputfile']}"), 'wt', encoding='UTF-8',newline='') as j:
                csv_match = csv.writer(j)
                header_match = ['2_theta_1', 'intensity_1', '2_theta_2', 'intensity_2', '2_theta_3', 'intensity_3', 'material_name', 'material_formula']
                csv_match.writerow(header_match)     
                csv_match.writerow(match)
            
    else: 
        print('Missing argument.')
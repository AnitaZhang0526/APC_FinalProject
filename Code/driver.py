# driver for the suite

import argparse
import csv
import os

import pandas as pd
import numpy as np

from ExperimentalTechnique_Factory import ExperimentalTechnique_Factory as ET_Factory
from PeakProfileFitting_Factory import PeakProfileFitting_Factory as PPF_Factory
from strategy import Strategy

# Test using `python driver.py -d XRD -m "Rietveld" -f "fast" -c 0.9 -r "5,15" -i 1-1-4-11_pH0_3-17-2020.csv`
parser = argparse.ArgumentParser(description='Analyzes results from XRD and FTIR output data.')
parser.add_argument('-d', '--data', type=str, 
    help='Type of data being uploaded, "XRD" or "FTIR".')
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

if __name__ == '__main__':
    args = vars(parser.parse_args())

    if args['data'] and args['method'] and args['cutoff'] and args['range'] and args['inputfile']:
        dir = os.path.dirname(os.path.realpath(__file__))

        input_path = os.path.join(dir, 'Input', str(args['inputfile']))
        spectrum = pd.read_csv(input_path, skiprows=2, header=None, names=['x','y'])
        spectrum['y']=spectrum['y']/max(spectrum['y'])

        technique = ET_Factory.factory_method(args['data'], spectrum)

        if (args['method'] == 'Rietveld'):
            if args['cutoff']:
                cutoff = float(args['cutoff'])
            else:
                cutoff = 0.9
            if args['range']:
                peak_widths_range = args['range'].split(',')
            else: 
                peak_widths_range = [5, 15]
            peak_widths = np.arange(int(peak_widths_range[0]),int(peak_widths_range[1]))
            strategy = Strategy()
            analysis = PPF_Factory.factory_method(args['method'], cutoff, peak_widths, spectrum, strategy)
            peak_indices = analysis.get_peaks()

            L = peak_indices.shape[0]
            model_choices = []
            for i in range(L):
                model_choices.append('GaussianModel')
            spec = strategy.make_one_spec(model_choices, peak_indices, spectrum['x'], spectrum['y'], peak_widths)
            composite_model, params = analysis.make_one_model(spec)
            peaks = analysis.get_peaks_params(args['fitting'])
            print(peaks)
            with open(os.path.join('Output', f"{args['inputfile']}.csv"), 'wt', encoding='UTF-8',newline='') as h:
                csv_peaks = csv.writer(h)
                header_peaks = ['FWHM', 'center', 'intensity', 'type']
                csv_peaks.writerow(header_city)
                for each in peaks:     
                    entry = [each.FWHM, each.center, each.intensity, each.type]
                    csv_peaks.writerow(entry)

    else: 
        print('Missing argument.')
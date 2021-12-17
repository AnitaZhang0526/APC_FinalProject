# imports
import numpy as np
import pandas as pd
import scipy.interpolate as interpolate
from Code.peak_profile_fitting import PeakProfileFitting
from Code.peak import Peak

"""
a subclass of PeakProfileFitting, a way to quickly profile fit
"""
class Poly(PeakProfileFitting):
    """
    : Poly inherits from PeakProfileFitting
    : The class has five properties: 
    : x: type double, from PeakProfileFitting
    : I: type double, from PeakProfileFitting
    : cutoff: type double, a cutoff frequency for rough filtering for initial peak approximation
    : peak_widths: type double array, a range that the a peak's width can fall between
    : strategy: Strategy object, an object that contain choices regarding the optimization process 
    : The class requires a single input parameter:
    : spectrum: dataFrame containing x and y values
    """
     
    def __init__(self, spectrum):
        super().__init__(spectrum)    

    # this function uses spline-fitting to output the peak locations, heights, and widths 
    # as an (Nx3) array where N is the number of peaks found
    def get_peaks_params(self):

        # sort data by ascending x values 
        data = np.transpose([self.x, self.I])
        data = data[data[:,0].argsort()]
        
        two_theta, intensity = data[:, 0], data[:, 1]
        min_angle = np.min(two_theta)
        max_angle = np.max(two_theta)
        num_samples = len(two_theta)

        # 's' is the smoothing factor. When set to 0, the spline will interpolate 
        # through ALL data points - this makes the derivative noisy.Too large and the peaks 
        # become too flat. Too small and derivative is too noisy. Maybe it doesn't matter
        # if only a subset of the peaks are used in the look-up side of things
        # Note:'k=4' specifies the degree of the spline. It is 4 here so that 
        # the derivative will have degree 3 and then we can leverage the .roots() 
        # function, which is only supported for cubic splines
        spline = interpolate.UnivariateSpline(two_theta, intensity, k=4, s=0.05)

        # specify new domain for spline interpolation. note that 4 here just means
        # the spline function will plot 4x more points than the raw data. This value
        # could be increased until the resulting spline is sufficiently smooth.
        x = np.linspace(min_angle, max_angle, num_samples*4, endpoint=True)

        # get first derivative
        deriv = spline.derivative()

        # Find the zeros of the derivatives and the intensity values at these locations
        roots = deriv.roots()
        peak_loc = roots 
        peak_height = spline(peak_loc)

        # (CRUDELY) Estimate peak widths as the difference between neighboring peak 
        # locations. Note that this relies on the assumption that the spline fitting
        # is giving false extrema located on either side of the actual peak 
        numPeaks = len(peak_loc)
        peak_widths = np.zeros((numPeaks))
        for i in range(1, numPeaks - 1):
            peak_widths[i] = peak_loc[i+1] - peak_loc[i-1] 

        # compile peak parameters into Nx3 matrix where the first, second, and 
        # third columns represent the peak width, location, and intensity, respectively
        peak_params = np.transpose(np.array([peak_widths, peak_loc, peak_height]))
        
        # convert peak_params to a list of "peak" objects
        peaks = []
        for width, center, intensity in peak_params:
            peaks.append(Peak(width, center, intensity, 'polynomial'))
        
        

        return peaks

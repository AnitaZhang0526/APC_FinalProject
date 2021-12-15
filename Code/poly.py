# imports
import numpy as np
import pandas as pd
import scipy.interpolate as interpolate
from Code.peak_profile_fitting import PeakProfileFitting


class Poly(PeakProfileFitting):
     
    def __init__(self, spectrum):
        super().__init__(spectrum)    

    # this function uses spline-fitting to output the peak locations, heights, and widths 
    # as an (Nx3) array where N is the number of peaks found
    def get_peak_params(self):

        two_theta, intensity = self.x, self.I
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
        spline = interpolate.UnivariateSpline(two_theta, intensity, k=4, s=0)

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

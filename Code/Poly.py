# imports
import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial import Polynomial
import scipy.interpolate as interpolate

# this function accepts the string name of the XRD data file as an input argument
# and uses spline-fitting to output the peak locations and heights as an 
# (Nx2) matrix where N is the number of peaks
def get_peaks(raw_data):
    
    # read in and parse real data (I'm not sure what this does, I just saw it in Rietveld)
    # when i try to use the test data I get an error: 'no such file or directory'
    f = open(raw_data, 'r')
    data = np.genfromtxt(f, delimiter=' ')

    # note: must normalize intensities
    two_theta, intensity = data[:,0], data[:,1]/np.max(data[:,1])
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
    peaks = np.transpose(np.array([roots, spline(roots)]))
    
    return peaks


    # Plot for sanity check
#     plt.scatter(two_theta, intensity, label='True') # real data
#     plt.plot(x, spline(x), 'g', label='Spline') # spline
#     plt.plot(x, deriv(x), label='derivative')
#     plt.legend()
#     plt.title("True data vs fit using splines on Malli_80s.ASC")
#     plt.ylabel('Intensity (%)')
#     plt.xlabel('$2\\theta$')
#     plt.xlim(5,10)
#     plt.ylim(0,1);





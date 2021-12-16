import cProfile
from Code.rietveld import Rietveld
from Code.rietveld_old import Rietveld_old
import numpy as np
import pandas as pd

f = open('Malli_80s.allASC.ASC', 'r')
data = np.genfromtxt(f, delimiter=' ')
x = data[:,0]
I = data[:,1]
I = I/max(I)
spectrum = pd.DataFrame({'x':x,'y':I})

rietveld_old = Rietveld_old(x,I)

if __name__ == '__main__':
    cutoff = 0.9
    peak_widths = np.arange(5,15) 
    peak_indices = rietveld_old.get_peaks(cutoff,peak_widths)
    cProfile.run('rietveld_old.find_best_fit(peak_widths,peak_indices)')
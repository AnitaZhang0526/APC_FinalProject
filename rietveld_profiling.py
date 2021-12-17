import cProfile
from Code.rietveld import Rietveld
import numpy as np
import pandas as pd
from Code.strategy import Strategy

f = open('Malli_80s.allASC.ASC', 'r')
data = np.genfromtxt(f, delimiter=' ')
x = data[:,0]
I = data[:,1]
I = I/max(I)
spectrum = pd.DataFrame({'x':x,'y':I})

cutoff = 0.9
peak_widths = np.arange(5,15) 

strategy = Strategy()
rietveld_new = Rietveld(cutoff,peak_widths,spectrum,strategy)

if __name__ == '__main__':
    choice = 'fast'
    cProfile.run('rietveld_new.find_best_fit(choice)')
import pytest
from Code.experimental_technique_factory import ExperimentalTechnique_Factory as ET_Factory
from Code.peak_profile_fitting_factory import PeakProfileFitting_Factory as PPF_Factory
from Code.xrd import XRD
from Code.ftir import FTIR
from Code.rietveld import Rietveld
from Code.strategy import Strategy
from Code.poly import Poly

def test_ET_Factory():
    spectrum, technique = ET_Factory.factory_method("1-1-4-11_pH0_3-17-2020.csv", "FTIR", True)
    assert(isinstance(technique,FTIR))

# def test_PPF_Factory():
#     spectrum, technique = ET_Factory.factory_method("1-1-4-11_pH0_3-17-2020.csv", "FTIR", True)
#     strategy = Strategy()
#     peaks, analysis = PPF_Factory.factory_method("Rietveld", "fast", 0.9, "5,15", spectrum, strategy, 0.2)
#     assert(isinstance(analysis,Rietveld))
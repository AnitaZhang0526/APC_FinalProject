import pytest
from src.experimental_technique_factory import ExperimentalTechnique_Factory as ET_factory
from src.xrd import XRD
from src.ftir import FTIR

def test_XRD_factory():
    inputfile = '1-1-4-11_pH0_3-17-2020.csv'
    input_type = 'XRD'
    transmittance = False
    spectrum, xrd = ET_factory.factory_method(inputfile, input_type, transmittance)
    assert(isinstance(xrd,XRD))
    
def test_FTIR_facotry():
    inputfile = '1-1-4-11_pH0_3-17-2020.csv'
    input_type = 'FTIR'
    transmittance = True
    spectrum, ftir = ET_factory.factory_method(inputfile, input_type, transmittance)
    assert(isinstance(ftir,FTIR))
    
def test_error_type():
    inputfile = 'Malli_80s.allASC.ASC'
    input_type = 'hello'
    transmittance = True
    with pytest.raises(ValueError):
        ET_factory.factory_method(inputfile, input_type, transmittance)
    

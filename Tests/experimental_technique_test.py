import pytest
from Code.experimental_technique_factory import ExperimentalTechnique_Factory as ET_factory
from Code.xrd import XRD
from Code.ftir import FTIR

def test_XRD_factory(spectrum):
    inputfile = 'Malli_80s.allASC.ASC'
    input_type = 'XRD'
    transmittance = False
    xrd = ET_factory.factory_method(inputfile, input_type, transmittance)
    assert(isinstance(xrd,XRD))
    
def test_FTIR_facotry(spectrum):
    inputfile = 'Malli_80s.allASC.ASC'
    input_type = 'FTIR'
    transmittance = True
    ftir = ET_factory.factory_method(inputfile, input_type, transmittance)
    assert(isinstance(p,Poly))
    
def test_error_type():
    inputfile = 'Malli_80s.allASC.ASC'
    input_type = 'hello'
    transmittance = True
    with pytest.raises(ValueError):
        ET_factory.factory_method(inputfile, input_type, transmittance)
    
# Tests for compare_to_database.py

from Code.compare_to_database import CompareToDatabase
from Code.peak import Peak
from unittest import mock

@mock.patch.object(CompareToDatabase, "_match_xrd")
def test_match_xrd(mock):
	CompareToDatabase("xrd").match()
	mock.assert_called()

@mock.patch.object(CompareToDatabase, "_match_ftir")
def test_match_ftir(mock):
	CompareToDatabase("ftir").match()
	mock.assert_called()

@mock.patch.object(CompareToDatabase, "_match_ftir")
@mock.patch.object(CompareToDatabase, "_match_xrd")
def test_match_none(mock_xrd, mock_ftir):
	CompareToDatabase().match()
	mock_xrd.assert_not_called()
	mock_ftir.assert_not_called()

@mock.patch.object(CompareToDatabase, "_match_ftir")
@mock.patch.object(CompareToDatabase, "_match_xrd")
def test_match_random(mock_xrd, mock_ftir):
	CompareToDatabase("random string").match()
	mock_xrd.assert_not_called()
	mock_ftir.assert_not_called()

def test_match_xrd_anilite():
	# Entry in database:
	# 46.28,100,32.29,65,27.86,57,Anilite,Cu7S4
	peaks = [
		Peak(None,46.27,100,None),
		Peak(None,99.22,56,None),
		Peak(None,10,20,None),
		Peak(None,32.29,65,None),
		Peak(None,111.5845225,30.333,None),
		Peak(None,27.86,57,None),
	]
	match = CompareToDatabase("xrd", peaks).match()
	assert(match["material_name"] == "Anilite")

def test_xrd_no_match():
	# Entry in database to *not* match:
	# 46.28,100,32.29,65,27.86,57,Anilite,Cu7S4
	peaks = [
		Peak(None,46.28,10,None),
		Peak(None,99.22,100,None),
		Peak(None,10,20,None),
		Peak(None,32.29,65,None),
		Peak(None,111.5845225,30.333,None),
		Peak(None,27.86,57,None),
	]
	match = CompareToDatabase("xrd", peaks).match()
	assert(match == None)

def test_match_xrd_equal_intensity_peaks():
	# Entry in database:
	# 164.92,100,29.76,100,155.65,100,Bowieite,"(Rh,Ir,Pt)1.77S3"
	peaks = [
		Peak(None,46.28,10,None),
		Peak(None,155.65,100,None),
		Peak(None,29.76,100,None),
		Peak(None,32.29,65,None),
		Peak(None,164.92,100,None),
		Peak(None,27.86,57,None),
	]
	match = CompareToDatabase("xrd", peaks).match()
	assert(match["material_name"] == "Bowieite")

def test_match_xrd_barahonaite_al():
	# Entry in database:
	# 4.01,100,7.92,70,17.79,50,Barahonaite-(Al),"(Ca,Cu,Na,Fe+++,Al )12Al2(AsO4)8(OH,Cl)x•nH2O"
	peaks = [
		Peak(None,17.79,51,None),
		Peak(None,4.05,100,None),
		Peak(None,7.92,69,None),
		Peak(None,32.29,48,None),
		Peak(None,164.92,22,None),
		Peak(None,27.86,12,None),
	]
	match = CompareToDatabase("xrd", peaks).match()
	assert(match["material_name"] == "Barahonaite-(Al)")

def test_xrd_no_peaks():
	peaks = []
	match = CompareToDatabase("xrd", peaks).match()
	assert(match == None)

def test_xrd_only_one_peak():
	peaks = [
		Peak(None,16.99,100,None),
	]
	match = CompareToDatabase("xrd", peaks).match()
	assert(match == None)

def test_xrd_only_2_peaks():
	peaks = [
		Peak(None,16.99,100,None),
		Peak(None,6.90,10,None),
	]
	match = CompareToDatabase("xrd", peaks).match()
	assert(match == None)

def test_match_ftir_nitrile_rubber():
	# Entry in database:
	# nitrile rubber,Primpke et al. 2018,966.3,1435.0,2924.1,1.0,0.9508345,0.37627639
	peaks = [
		Peak(None,966.3,1.0,None),
		Peak(None,262.5,0.103,None),
		Peak(None,1435.0,0.9508345,None),
		Peak(None,120.6,0.12,None),
		Peak(None,2914.4,0.25,None),
		Peak(None,2924.1,0.37627639,None),
	]
	match = CompareToDatabase("ftir", peaks).match()
	assert(match["name"] == "nitrile rubber")

def test_match_ftir_no_match():
	# Entry in database:
	# nitrile rubber,Primpke et al. 2018,966.3,1435.0,2924.1,1.0,0.9508345,0.3762763
	peaks = [
	Peak(None,3000.1,1.0,None),
		Peak(None,262.5,0.103,None),
		Peak(None,2500,0.9508345,None),
		Peak(None,120.6,0.12,None),
		Peak(None,2914.4,0.25,None),
		Peak(None,4000,0.37627639,None),
	]
	match = CompareToDatabase("ftir", peaks).match()
	assert(match == None)

def test_match_ftir_silicone_rubber():
	# Entry in database:
	# silicone rubber,Primpke et al. 2018,785.0,1006.8,1064.7,1.0,0.8293072,0.4721336
	peaks = [
		Peak(None,1064.7,0.4721336,None),
		Peak(None,384.5,0.2821336,None),
		Peak(None,150.6,0.2569874,None),
		Peak(None,1006.8,0.8293072,None),
		Peak(None,785.0,1.0,None),
		Peak(None,585.4,0.1721336,None),
	]
	match = CompareToDatabase("ftir", peaks).match()
	assert(match["name"] == "silicone rubber")


def test_ftir_no_peaks():
	peaks = []
	match = CompareToDatabase("ftir", peaks).match()
	assert(match == None)

def test_ftir_only_one_peak():
	peaks = [
		Peak(None,1542.1,1.0,None),
	]
	match = CompareToDatabase("ftir", peaks).match()
	assert(match == None)

def test_ftir_only_2_peaks():
	peaks = [
		Peak(None,1425.5,1.0,None),
		Peak(None,1543.8,1.0,None),
	]
	match = CompareToDatabase("ftir", peaks).match()
	assert(match == None)
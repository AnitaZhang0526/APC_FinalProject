# Tests for compare_to_database.py

from Code.compare_to_database import CompareToDatabase
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
		[46.27, 100],
		[99.22, 56],
		[10, 20],
		[32.29, 65],
		[111.5845225, 30.333],
		[27.86, 57],
	]
	match = CompareToDatabase("xrd", peaks).match()
	assert(match["material_name"] == "Anilite")

def test_match_xrd_right_location_wrong_intensity():
	# Entry in database to *not* match:
	# 46.28,100,32.29,65,27.86,57,Anilite,Cu7S4
	peaks = [
		[46.28, 10],
		[99.22, 100],
		[10, 20],
		[32.29, 65],
		[111.5845225, 30.333],
		[27.86, 57],
	]
	match = CompareToDatabase("xrd", peaks).match()
	assert(match["material_name"] != "Anilite")

def test_match_xrd_equal_intensity_peaks():
	# Entry in database:
	# 164.92,100,29.76,100,155.65,100,Bowieite,"(Rh,Ir,Pt)1.77S3"
	peaks = [
		[46.28, 10],
		[155.65, 100],
		[29.76, 100],
		[32.29, 65],
		[164.92, 100],
		[27.86, 57],
	]
	match = CompareToDatabase("xrd", peaks).match()
	assert(match["material_name"] == "Bowieite")

def test_match_xrd_barahonaite_al():
	# Entry in database:
	# 4.01,100,7.92,70,17.79,50,Barahonaite-(Al),"(Ca,Cu,Na,Fe+++,Al )12Al2(AsO4)8(OH,Cl)x•nH2O"
	peaks = [
		[17.79, 51],
		[4.05, 100],
		[7.92, 69],
		[32.29, 48],
		[164.92, 22],
		[27.86, 12],
	]
	match = CompareToDatabase("xrd", peaks).match()
	assert(match["material_name"] == "Barahonaite-(Al)")

def test_xrd_no_peaks():
	peaks = []
	match = CompareToDatabase("xrd", peaks).match()
	assert(match == None)

def test_xrd_only_one_peak():
	peaks = [
		[16.99, 100],
	]
	match = CompareToDatabase("xrd", peaks).match()
	assert(match == None)

def test_xrd_only_2_peaks():
	peaks = [
		[16.99, 100],
		[6.90, 10],
	]
	match = CompareToDatabase("xrd", peaks).match()
	assert(match == None)

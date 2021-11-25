# Tests for compare_to_database.py

from Code.compare_to_database import CompareToDatabase
from unittest import mock

@mock.patch.object(CompareToDatabase, "_match_xrd")
def test_match_xrd(mock):
	CompareToDatabase('xrd').match()
	mock.assert_called()

@mock.patch.object(CompareToDatabase, "_match_ftir")
def test_match_ftir(mock):
	CompareToDatabase('ftir').match()
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
	CompareToDatabase('random string').match()
	mock_xrd.assert_not_called()
	mock_ftir.assert_not_called()

def test_match_xrd_anilite():
	# 46.28,100,32.29,65,27.86,57,Anilite,Cu7S4
	assert(False)

def test_match_xrd_barahonaite_al():
	# 4.01,100,7.92,70,17.79,50,Barahonaite-(Al),"(Ca,Cu,Na,Fe+++,Al )12Al2(AsO4)8(OH,Cl)x•nH2O"
	assert(False)

def test_match_xrd_two_matches():
	# Halfway between these two
	# 4.01,100,7.92,70,17.79,50,Barahonaite-(Al),"(Ca,Cu,Na,Fe+++,Al )12Al2(AsO4)8(OH,Cl)x•nH2O"
	# 4.01,100,7.89,70,32.38,30,Barahonaite-(Fe),"(Ca,Cu,Na,Fe+++,Al )12Fe+++2(AsO4)8(OH,Cl)x•nH2O"
	assert(False)

def test_xrd_only_one_peak():
	assert(False)

def test_xrd_only_2_peaks():
	assert(False)

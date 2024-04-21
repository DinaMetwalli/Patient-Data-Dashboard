import pytest
import os
from src.filter.filter import Filter

def test_filter_by_referral():
    global csv_path

    filter = Filter()

    root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    csv_path = os.path.join(root_directory, "src/CSVParser/Data.csv")
    
    referral_status = True
    filtered_data = filter.filter_by_referral(referral_status, csv_path)
    
    assert isinstance(filtered_data, list)

def test_filter_by_bmi():

    filter = Filter()
    
    bmi = 27
    filtered_data = filter.filter_by_bmi(bmi, csv_path)
    assert isinstance(filtered_data, list)
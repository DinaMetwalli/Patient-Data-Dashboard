import pytest
import os
import pandas as pd
from src.CSVParser.CSVParser import ParseCSV 

def test_import_csv():
    global parser
    parser = ParseCSV()

    test_csv_path = 'test.csv'
    test_data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    test_data.to_csv(test_csv_path, index=False)
    
    imported_data = parser.import_csv(test_csv_path)
    assert isinstance(imported_data, pd.DataFrame)

    os.remove(test_csv_path)

def test_import_csv_nonexistent_file():
    with pytest.raises(Exception):
        parser.import_csv('nonexistent.csv')

def test_export_csv():
 
    export_path = 'exported.csv'
    test_data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    parser.export_csv(test_data, export_path)
    assert os.path.exists(export_path)

    os.remove(export_path)

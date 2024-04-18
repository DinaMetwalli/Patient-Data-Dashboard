import csv
import os
import pandas as pd
import numpy as np
from pathlib import Path

class ParseCSV():
    _instance = None
    
    def __init__(self):
        self.data = []
        self.features = []

    @classmethod
    def get_instance(cls, ccu):
        if cls._instance is None:
            cls._instance = cls(ccu)

        return cls._instance
    
    def import_csv(self, import_name: str) -> pd.DataFrame:
        """
        Imports the given CSV file

        Parameters:
            import_name (str): name of CSV file to be imported and parsed

        Returns:
            self.data (DataFrame): parsed data
        """
        file_path = import_name
        
        if os.path.exists(file_path):
            # Load the CSV file
            self.data = pd.read_csv(file_path)
            self.data = self.data.replace(np.nan, None)

            print("CSV file imported successfully.")
            
            return self.data
        
        else:
            raise Exception("File not found.")

    def export_csv(self, data: pd.DataFrame, export_name:str = None) -> None:
        """
        Exports the parsed CSV file

        Parameters:
            export_name (str): name of CSV file to be exported
        """
        try:
            if data is not None:
                # Export DataFrame to CSV
                if export_name is None:
                    root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
                    result_file = os.path.join(root_directory, "Analysis_Results.csv")
                    data.to_csv(result_file, index=False)
                else:
                    desktop_path = Path.home() / "Desktop"
                    analysed_data_path = desktop_path / "Analysed Data"
                    
                    if not os.path.exists(analysed_data_path):
                        os.mkdir(analysed_data_path)
                        
                    data.to_csv(analysed_data_path / export_name, index=False)

                print("CSV file exported successfully.")
            
            else:
                print("No data to export.") 
        except Exception as e:
            print("An error occurred while exporting CSV:", e)
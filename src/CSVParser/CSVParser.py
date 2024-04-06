import csv
import os
import pandas as pd
import numpy as np

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
    
    def import_csv(self, import_name: str) -> pd.DataFrame | None:
        file_path = f"src/CSVParser/{import_name}"
        
        if os.path.exists(file_path):
            # Load the CSV file
            self.data = pd.read_csv(file_path)
            self.data = self.data.replace(np.nan, None)

            print("CSV file imported successfully.")
            
            return self.data
        
        else:
            print("File not found.")

    def export_csv(self, export_name: str) -> None:
        try:
            if self.data is not None:
                # Export DataFrame to CSV
                self.data.to_csv(export_name, index=False)

                print("CSV file exported successfully.")
            
            else:
                print("No data to export.") 
        except Exception as e:
            print("An error occurred while exporting CSV:", e)
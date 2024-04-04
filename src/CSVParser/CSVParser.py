import csv
import os
import pandas as pd

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
    
    def import_csv(self):
        file_path = "src/CSVParser/Data.csv"
        if os.path.exists(file_path):
            # Load the CSV file
            self.data = pd.read_csv(file_path)
            self.data.fillna(value="", inplace=True)
            print("CSV file imported successfully.")
        else:
            print("File not found.")

    def export_csv(self):
        try:
            if self.data is not None:
                print(self.data)
                # Export DataFrame to CSV
                self.data.to_csv("ExportedData.csv", index=False)
                print("CSV file exported successfully.")
            else:
                print("No data to export.") 
        except Exception as e:
            print("An error occurred while exporting CSV:", e)


# Create an instance of the class
parser = ParseCSV()

# Call the import_csv method
parser.import_csv()
parser.export_csv()
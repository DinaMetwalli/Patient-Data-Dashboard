from ..CSVParser.CSVParser import ParseCSV
import pandas as pd


class Filter:
    def __init__(self):
        self.patients = None
        self.parse_csv = ParseCSV()

    def filter(self):
        # Import CSV data
        self.parse_csv.import_csv()
        self.patients = self.parse_csv.data

    def filter_by_referral(self, referral):
        if self.patients is None or len(self.patients) == 0:
            self.filter()
        # Convert the 'referral' column to float for comparison
        self.patients['referral'] = self.patients['referral'].astype(float)
        filtered_data = self.patients[self.patients['referral'] == referral]
        return filtered_data

    def filter_by_bmi(self, bmi):
        if self.patients is None or len(self.patients) == 0:
            self.filter()
        # Filter out empty strings in 'bmi' column
        filtered_data = self.patients[self.patients['bmi'].astype(str).str.strip() != '']
        filtered_data['bmi'] = pd.to_numeric(filtered_data['bmi'], errors='coerce')  # Convert to numeric, coerce errors
        filtered_data = filtered_data[round(filtered_data['bmi']) == round(bmi)]
        return filtered_data


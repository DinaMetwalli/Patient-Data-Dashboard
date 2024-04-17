from ..CSVParser.CSVParser import ParseCSV
import pandas as pd


class Filter:
    def __init__(self):
        self.patients_data = None
        self.parser = ParseCSV()

    def filter(self, csv_path):
        # Import CSV data
        self.patients_data = self.parser.import_csv(csv_path)

    def filter_by_referral(self, referral, csv_path):
        if self.patients_data is None or len(self.patients_data) == 0:
            self.filter(csv_path)

        if referral is not False:
            status = 1.0
        else:
            status = 0.0

        print(status)
        
        filtered_patients_data = []

        # Convert 'referral' column to float
        self.patients_data['referral'] = self.patients_data['referral'].astype(float)
        filtered_data = self.patients_data[self.patients_data['referral'] == status]
    
        if not filtered_data.empty:
            for index, row in filtered_data.iterrows():
                patient_data = {}
                for column in self.patients_data.columns:
                    patient_data[column] = row[column]
                filtered_patients_data.append(patient_data)

        return filtered_patients_data

    def filter_by_bmi(self, bmi, csv_path):
        if self.patients_data is None or len(self.patients_data) == 0:
            self.filter(csv_path)

        bmi_prefix = str(bmi)[:2]
        filtered_patients_data = []
        
        bmi_data = self.patients_data.copy()
        # Find two first digits of each bmi column and convert them to string
        bmi_data['bmi_prefix'] = bmi_data['bmi'].astype(str).str[:2]
        filtered_data = bmi_data[bmi_data['bmi_prefix'] == bmi_prefix]
        
        if not filtered_data.empty:
            for index, row in filtered_data.iterrows():
                patient_data = {}
                for column in self.patients_data.columns:
                    patient_data[column] = row[column]
                filtered_patients_data.append(patient_data)

        return filtered_patients_data
from .DietaryRequirements import DietaryRequirements

from src.CSVParser.CSVParser import ParseCSV

import pandas as pd

class Patient():
    def __init__(self, patient_id, csv_file) -> None:
        self.patient_id = patient_id
        self.csv_file = csv_file

        self.referral = 0
        self.patient_data = {}
        self.parser = ParseCSV()
        
        self.fetch_all_patients_data()

    def parse_csv_data(self) -> pd.DataFrame:
        """
        Uses Parser to parse provided CSV file.

        Returns:
            self.data (DataFrame): parsed data
        """
        self.data = self.parser.import_csv(self.csv_file)

        return self.data
    
    def fetch_all_patients_data(self) -> dict:
        """
        Fetches records of all patients from the parsed data

        Returns:
            self.patient_data (dict): dictionary of patient data
        """
        data = self.parse_csv_data()

        filtered_data = data[data["encounterId"] == self.patient_id]

        if not filtered_data.empty:
            for column in filtered_data.columns:
                if (column != "encounterId") and (column != "referral"):
                    self.patient_data[column] = [filtered_data[column].iloc[0]]

            for value in self.patient_data:
                if self.patient_data[value][0] != None:
                    self.patient_data[value][0] = round(self.patient_data[value][0], 2)
            
            return self.patient_data
        else:
            raise Exception(f"No matching records found for patient {self.patient_id}.")
    
    def get_referral_status(self) -> bool:
        return self.referral
    
    def dietary_req(self) -> DietaryRequirements:
        return DietaryRequirements(self.patient_id, self.patient_data)
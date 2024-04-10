from .DietaryRequirements import DietaryRequirements
from .RespiratoryMeasurments import RespiratoryMeasurments

from src.CSVParser.CSVParser import ParseCSV

import pandas as pd

class Patient():
    def __init__(self, csv_file: str, patient_id: int = None):
        self.csv_file = csv_file
        self.patient_id = patient_id

        self.referral = 0
        self.patient_data = {}
        self.parser = ParseCSV()

        if patient_id is not None:
            self.fetch_patient_data(self.patient_id)

    def parse_csv_data(self) -> pd.DataFrame:
        """
        Uses Parser to parse provided CSV file.

        Returns:
            self.data (DataFrame): parsed data
        """
        return self.parser.import_csv(self.csv_file)
    
    def fetch_all_patient_data(self) -> list:
        """
        Fetches records of all patients from the parsed data

        Returns:
            patients_data (list): a list of dictionaries, each containing each patient's data
        """
        data = self.parse_csv_data()

        patients_data = []

        for index, row in data.iterrows():
            patient_data = {}
            for column in data.columns:
                patient_data[column] = row[column]
            patients_data.append(patient_data)

        return patients_data
    
    def fetch_patient_data(self, patient_id) -> dict:
        """
        Fetches a specific patient's data from the parsed data.

        Parameters:
            patient_id (int): the ID of the patient to have their data fetched

        Returns:
            self.patient_data (dict): a dictionary of a the patient's data
        """
        data = self.parse_csv_data()

        filtered_data = data[data["encounterId"] == patient_id]

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
        
    def calculate_average_data(self) -> dict:
        """
        Calculates overall average of patient data

        Returns:
            averages (dict): a dictionary of calculated averages
                             maps the value to its total and count
        """
        patient_data = self.parse_csv_data()

        measurements = {}
        for column in patient_data.columns:
            if (column != "encounterId") and (column != "referral"):
                measurements[column] = {"total": 0, "count": 0}

        for index, row in patient_data.iterrows():
            for variable, data in measurements.items():
                value = row[variable]
                if value is not None:
                    data["total"] += value
                    data["count"] += 1

        # Calculate averages of all patient data
        averages = {variable: data["total"] / data["count"] if data["count"] != 0 else 0 for variable, data in measurements.items()}
        for data in averages:
            averages[data] = round(averages[data], 2)

        return averages
    
    def get_referral_status(self) -> bool:
        """Get patient's referral status"""
        # Note: if ML algorithm saves output to CSV file, this function is correct,
        # as a patient's instance could be created with the path of the resulted CSV,
        # and this will function the same.
        return self.referral
    
    def dietary_req(self) -> DietaryRequirements:
        """Get patient's dietary requirement data"""
        return DietaryRequirements(self.patient_id, self.patient_data)
    
    def resp_measurments(self) -> RespiratoryMeasurments:
        """Get patient's respiratory measurements data"""
        return RespiratoryMeasurments(self.patient_id, self.patient_data)
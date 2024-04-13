from src.CSVParser.CSVParser import ParseCSV
from ..Patients.Patients import Patient
from .AverageReport import AverageReport
from .PatientReport import PatientReport

import pandas as pd

class Report():
    def __init__(self) -> None:
        self.parser = ParseCSV()
    
    def fetch_average_data(self, csv_path: str) -> dict:
        """
        Fetches average data of all patients

        Parameters:
            csv_path (str): CSV file to fetch data from

        Returns:
            (dict): a dictionary of all patients averages
        """
        patient = Patient(csv_path)
        return patient.calculate_average_data()
    
    def fetch_patient_data(self, csv_path: str, patient_id: int) -> dict:
        """
        Fetches data of specific patient

        Parameters:
            csv_path (str): CSV file to fetch data from
            patient_id (int): the patient's encounter ID

        Returns:
            (dict): a dictionary of all patients averages
        """
        patient = Patient(csv_path)
        return patient.fetch_patient_data(patient_id)
    
    def average(self, csv_path: str) -> AverageReport:
        """
        Accesses Average Report methods

        Parameters:
            csv_path (str): CSV file to fetch data from

        Returns:
            (object): an instance of AverageReport
        """
        average_data = self.fetch_average_data(csv_path)
        return AverageReport(average_data)
    
    def patient(self, patient_id: int, csv_path: str) -> PatientReport:
        """
        Accesses Patient Report methods

        Parameters:
            csv_path (str): CSV file to fetch data from
            patient_id (int): the patient's encounter ID

        Returns:
            (object): an instance of PatientReport
        """
        patient_data = self.fetch_patient_data(csv_path, patient_id)
        average_data = self.fetch_average_data(csv_path)
        return PatientReport(patient_data, average_data, patient_id)
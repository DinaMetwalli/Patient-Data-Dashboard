from src.CSVParser.CSVParser import ParseCSV
from ..Patients.Patients import Patient
from .AverageReport import AverageReport
from .PatientReport import PatientReport

import pandas as pd

class Report():
    def __init__(self) -> None:
        self.parser = ParseCSV()
    
    def fetch_average_data(self, csv_path) -> dict:
        patient = Patient(csv_path)
        return patient.calculate_average_data()
    
    def fetch_patient_data(self, csv_path, patient_id) -> dict:
        patient = Patient(csv_path)
        return patient.fetch_patient_data(patient_id)
    
    def average(self, csv_path) -> AverageReport:
        average_data = self.fetch_average_data(csv_path)
        return AverageReport(average_data)
    
    def patient(self, patient_id, csv_path) -> PatientReport:
        patient_data = self.fetch_patient_data(csv_path, patient_id)
        average_data = self.fetch_average_data(csv_path)
        return PatientReport(patient_data, average_data, patient_id)
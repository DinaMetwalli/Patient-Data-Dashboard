from .Authenticator import Authenticator
from ..utils.errors import AuthorizationError
from ..CSVParser.CSVParser import ParseCSV
from ..Patients.Patients import Patient
from ..Reports.ReportGenerator import Report
from ..analyser.algorithm import MLAlgorithm

class CCU():
    
    def __init__(self):
        self.auth = Authenticator()

    def entry(self, passkey: str) -> bool:
        if not self.auth.validate_entry_passkey(passkey):
            raise AuthorizationError("Incorrect Passkey")
        return True
    
    def import_password(self, password: str) -> bool:
        if not self.auth.validate_import_password(password):
            raise AuthorizationError("Incorrect Import Password")
        return True

    def export_password(self, password: str) -> bool:
        if not self.auth.validate_export_password(password):
            raise AuthorizationError("Incorrect Export Password")
        return True
    
    def csv_parser(self) -> ParseCSV:
        """access CSV Parser methods"""
        return ParseCSV()
    
    def patients(self, csv_file, patient_id: int = None) -> Patient:
        """access Patient methods"""
        return Patient(csv_file, patient_id)
    
    def reports(self) -> Report:
        """access Report methods"""
        return Report()
    
    def algorithm(self) -> MLAlgorithm:
        """access ML algorithm methods"""
        return MLAlgorithm()
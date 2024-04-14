from .Authenticator import Authenticator
from ..utils.errors import AuthorizationError
from ..CSVParser.CSVParser import ParseCSV
from ..Patients.Patients import Patient
from ..Reports.ReportGenerator import Report

class CCU():
    
    def __init__(self):
        self.auth = Authenticator()

    def entry_password(self, passkey: str) -> bool:
        if not self.auth.validate_entry_passkey(passkey):
            raise AuthorizationError("Incorrect Passkey")
        return True
    
    def import_password(self, password: str) -> bool:
        if not self.auth.validate_import_passkey(password):
            raise AuthorizationError("Incorrect Import Passkey")
        return True

    def export_password(self, password: str) -> bool:
        if not self.auth.validate_export_passkey(password):
            raise AuthorizationError("Incorrect Export Passkey")
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
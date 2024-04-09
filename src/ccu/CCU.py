from .Authenticator import Authenticator
from ..utils.errors import AuthorizationError
from ..CSVParser.CSVParser import ParseCSV
from ..Patients.Patients import Patient
from ..Reports.ReportGenerator import Report

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
        return ParseCSV()
    
    def patients(self) -> Patient:
        return Patient
    
    def reports(self) -> Report:
        return Report
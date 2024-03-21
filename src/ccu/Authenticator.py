class Authenticator():

    def __init__(self):
        self.passkey = "passkey"
        self.import_pass = "import"
        self.export_pass = "export"
    
    def validate_entry_passkey(self, passkey: str) -> bool:
        return self.passkey == passkey
    
    def validate_import_password(self, passkey: str) -> bool:
        return self.import_pass == passkey
    
    def validate_export_password(self, passkey: str) -> bool:
        return self.export_pass == passkey
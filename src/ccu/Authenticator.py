import binascii
import hashlib
import os
import json

class Authenticator():
    def __init__(self) -> None:
        self.file = "config.json"
    
    def hash_password(self, password: str, salt=None) -> str:
        if salt is None:
            salt = os.urandom(16)
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        my_pass = binascii.hexlify(salt + key).decode('utf-8')
        return my_pass

    def validate_entry_passkey(self, input_password: str) -> bool:
        stored_passwords = self.load_passwords()
        stored_password = stored_passwords.get("ENTRY_PASSWORD")
        if stored_password is not None:
            return self.verify_password(stored_password, input_password)
        else:
            raise Exception("No passkey set for entry")

    def validate_import_passkey(self, input_password: str) -> bool:
        stored_passwords = self.load_passwords()
        stored_password = stored_passwords.get("IMPORT_PASSWORD")
        if stored_password is not None:
            return self.verify_password(stored_password, input_password)
        else:
            raise Exception("No passkey set for import")

    def validate_export_passkey(self, input_password: str) -> bool:
        stored_passwords = self.load_passwords()
        stored_password = stored_passwords.get("EXPORT_PASSWORD")
        if stored_password is not None:
            return self.verify_password(stored_password, input_password)
        else:
            raise Exception("No passkey set for export")

    def verify_password(self, stored_password: str, input_password: str) -> bool:
        decoded_stored_password = binascii.unhexlify(stored_password.encode('utf-8'))
        salt = decoded_stored_password[:16]
        stored_key = decoded_stored_password[16:]
        provided_key = hashlib.pbkdf2_hmac('sha256', input_password.encode('utf-8'), salt, 100000)

        return stored_key == provided_key
    
    def load_passwords(self) -> dict:
        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                return json.load(f)
        else:
            return {}
        
    def save_passwords(self, passwords: dict) -> None:
        with open(self.file, "w") as f:
            json.dump(passwords, f)
    
    def generate_passkeys(self, entry_passkey: str, import_passkey: str, export_passkey: str) -> None:
        hashed_entry_pass = self.hash_password(entry_passkey)
        hashed_import_pass = self.hash_password(import_passkey)
        hashed_export_pass = self.hash_password(export_passkey)

        passwords = {
            "ENTRY_PASSWORD": hashed_entry_pass,
            "IMPORT_PASSWORD": hashed_import_pass,
            "EXPORT_PASSWORD": hashed_export_pass
        }

        self.save_passwords(passwords)
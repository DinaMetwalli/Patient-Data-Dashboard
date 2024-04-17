import pytest
import os
import json
from src.ccu.Authenticator import Authenticator

@pytest.fixture
def auth():
    return Authenticator()


def test_validate_entry_passkey(auth):
    """Test the validation of the entry passkey."""
    auth.save_passwords({"ENTRY_PASSWORD": auth.hash_password("test123")})
    assert auth.validate_entry_passkey("test123")
    assert not auth.validate_entry_passkey("wrongpass")

def test_validate_import_passkey(auth):
    """Test the validation of the import passkey."""
    auth.save_passwords({"IMPORT_PASSWORD": auth.hash_password("test123")})
    assert auth.validate_import_passkey("test123")
    assert not auth.validate_import_passkey("wrongpass")

def test_validate_export_passkey(auth):
    """Test the validation of the export passkey."""
    auth.save_passwords({"EXPORT_PASSWORD": auth.hash_password("test123")})
    assert auth.validate_export_passkey("test123")
    assert not auth.validate_export_passkey("wrongpass")


def test_hash_password(auth):
    """Test hashing a password."""
    password = "test123"
    hashed_pass = auth.hash_password(password)
    assert len(hashed_pass) > 0

def test_verify_password(auth):
    """Test verifying a password."""
    password = "test123"
    hashed_pass = auth.hash_password(password)
    assert auth.verify_password(hashed_pass, password)

def test_password_storage(auth, tmp_path):
    """Test storing and retrieving passwords."""
    file_path = tmp_path / "test_config.json"
    auth.file = str(file_path)
    
    # Save passwords
    passwords = {"ENTRY_PASSWORD": auth.hash_password("test123")}
    auth.save_passwords(passwords)

    # Load passwords and verify
    loaded_passwords = auth.load_passwords()
    assert "ENTRY_PASSWORD" in loaded_passwords

def test_load_passwords(auth, tmp_path):
    """Test loading passwords from a file."""
    file_path = tmp_path / "test_config.json"
    with open(file_path, "w") as f:
        json.dump({"ENTRY_PASSWORD": auth.hash_password("test123")}, f)
    auth.file = str(file_path)
    passwords = auth.load_passwords()
    assert "ENTRY_PASSWORD" in passwords

def test_save_passwords(auth, tmp_path):
    """Test saving passwords to a file."""
    file_path = tmp_path / "test_config.json"
    auth.file = str(file_path)
    passwords = {"ENTRY_PASSWORD": auth.hash_password("test12232323")}
    auth.save_passwords(passwords)
    with open(file_path, "r") as f:
        saved_passwords = json.load(f)
    assert "ENTRY_PASSWORD" in saved_passwords

def test_generate_passkeys(auth, tmp_path):
    """Test generating passkeys."""
    file_path = tmp_path / "test_config.json"
    auth.file = str(file_path)
    
    # Generate passkeys
    entry_passkey = "entrypass"
    import_passkey = "importpass"
    export_passkey = "exportpass"
    auth.generate_passkeys(entry_passkey, import_passkey, export_passkey)

    # Load generated passkeys and verify
    loaded_passwords = auth.load_passwords()
    assert "ENTRY_PASSWORD" in loaded_passwords
    assert "IMPORT_PASSWORD" in loaded_passwords
    assert "EXPORT_PASSWORD" in loaded_passwords

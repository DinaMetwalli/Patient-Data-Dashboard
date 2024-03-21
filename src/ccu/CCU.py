from .Authenticator import Authenticator
from ..utils.errors import AuthorizationError

class CCU():
    
    def __init__(self):
        self.auth = Authenticator()

    def entry(self, passkey: str) -> bool:
        if not self.auth.validate_entry_passkey(passkey):
            raise AuthorizationError("Incorrect Passkey")
        return True
    
    def import_password(self,password: str) -> None:
        if not self.auth.validate_import_password(password):
            raise AuthorizationError("Incorrect Import Password")
        return True
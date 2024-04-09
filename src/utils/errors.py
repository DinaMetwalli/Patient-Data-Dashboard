class RaiseError(Exception):
    """Base class for all system errors."""

    def __init__(self, message: str) -> None:
        """Create error message."""
        self.message = message


class AuthorizationError(RaiseError):
    """Error for when a user has incorrect access credentials."""


class InputError(RaiseError):
    """Error for when an invalid input is provided."""
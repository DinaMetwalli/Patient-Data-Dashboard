"""Module with HTTP responses."""
from enum import Enum
from typing import Any
from flask import jsonify

class Status(Enum):
    """Enum with http status code."""

    OK = 200
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    CONFLICT = 409


def OK(data: dict[str, Any], success: bool = True, code: Status = Status.OK):
    """Call for OK HTTP Status."""
    return jsonify({
        "success": success,
        "data": data,
    }), code.value

def Error(code: Status, message: str, details: dict[str, Any] = {}):
    """Get Error HTTP Status response."""
    return jsonify({
        "success": False,
        "message": message,
        "details": details
    }), code.value
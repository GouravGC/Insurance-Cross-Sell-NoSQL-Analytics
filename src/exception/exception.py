"""
Custom exception handling for the application.
"""
import sys
import traceback
from typing import Optional

from src.logger.logger import get_logger

logger = get_logger(__name__)


class AppException(Exception):
    """Custom exception class that captures detailed error information."""

    def __init__(
        self,
        message: str,
        error: Optional[Exception] = None,
        error_detail: Optional[traceback.StackSummary] = None,
    ):
        super().__init__(message)
        self.message = message
        self.error = error
        self.error_detail = error_detail or traceback.extract_stack()

    def __str__(self) -> str:
        return f"{self.message}"

    def to_dict(self) -> dict:
        return {
            "message": self.message,
            "error": repr(self.error) if self.error else None,
            "traceback": "".join(
                traceback.format_list(self.error_detail)
            ).strip(),
        }


def handle_exception(exc: Exception, context: str = "") -> None:
    """Log an exception with context and optionally raise AppException."""
    logger.error("Exception in %s: %s", context, exc, exc_info=True)
    tb = traceback.format_exc()
    logger.error("Traceback:\n%s", tb)


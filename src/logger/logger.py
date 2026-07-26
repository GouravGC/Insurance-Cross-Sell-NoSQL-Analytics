"""
Logging configuration for the application.
Logs are written to both console and a rotating log file.
Uses a safe console handler that replaces unencodable characters (emojis, etc.)
for Windows compatibility.
"""
import logging
import sys
from pathlib import Path
from logging.handlers import RotatingFileHandler

_LOG_DIR = Path(__file__).resolve().parent.parent.parent / "logs"
_LOG_FILE = _LOG_DIR / "app.log"
_LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
_LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
_MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB
_BACKUP_COUNT = 3


class EncodingSafeStreamHandler(logging.StreamHandler):
    """StreamHandler that replaces characters not supported by the console encoding."""

    def emit(self, record):
        try:
            super().emit(record)
        except UnicodeEncodeError:
            # Replace characters that can't be encoded by the console
            msg = self.format(record)
            try:
                stream = self.stream
                encoded = msg.encode(stream.encoding, errors="replace").decode(
                    stream.encoding
                )
                stream.write(encoded + self.terminator)
                self.flush()
            except Exception:
                self.handleError(record)


def setup_logger(name: str = "app") -> logging.Logger:
    """Create and configure a logger instance."""
    _LOG_DIR.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    # File handler (rotating)
    file_handler = RotatingFileHandler(
        _LOG_FILE, maxBytes=_MAX_LOG_SIZE, backupCount=_BACKUP_COUNT
    )
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(_LOG_FORMAT, datefmt=_LOG_DATE_FORMAT)
    file_handler.setFormatter(file_formatter)

    # Console handler (encoding-safe for Windows)
    console_handler = EncodingSafeStreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt=_LOG_DATE_FORMAT,
    )
    console_handler.setFormatter(console_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


def get_logger(name: str = "app") -> logging.Logger:
    """Retrieve an existing logger or create a new one."""
    return logging.getLogger(name) or setup_logger(name)


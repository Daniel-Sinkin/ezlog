import inspect
import logging
import os


def get_logger(
    level=logging.DEBUG,
    log_format="%(asctime)s [%(name)s] [%(levelname)s] %(message)s",
    stream_handler=True,
    filename=None,
):
    """
    Sets up and returns a logger configured with the given parameters.

    Parameters:
    - level: The logging level (default: logging.DEBUG)
    - log_format: The format for log messages (default: standard format with timestamp, logger name, and level)
    - stream_handler: Whether to output logs to the console (default: True)
    - filename: Optional filename to log to a file instead of the console (default: None)

    Returns:
    - logger: Configured logger instance
    """

    # Get the name of the calling file (the script that imports and uses ezlog)
    caller_frame = inspect.stack()[1]
    caller_filename = os.path.basename(caller_frame.filename)

    # Create a logger with the caller's filename
    logger = logging.getLogger(caller_filename)

    # Set the logging level
    logger.setLevel(level)

    # Create a formatter with the specified format
    formatter = logging.Formatter(log_format)

    # Clear any existing handlers to avoid duplicate logs
    if logger.hasHandlers():
        logger.handlers.clear()

    # Add a StreamHandler to log to the console, if specified
    if stream_handler:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    # Add a FileHandler to log to a file, if specified
    if filename:
        file_handler = logging.FileHandler(filename)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

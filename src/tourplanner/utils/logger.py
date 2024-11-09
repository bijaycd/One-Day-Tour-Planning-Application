import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("tourplanner.log"),  # Log to a file
        logging.StreamHandler()  # Log to the console
    ]
)

# Get the logger
logger = logging.getLogger("tourplanner")

def log_info(message):
    """
    Log an informational message.
    Args:
        message (str): The message to log.
    """
    logger.info(message)

def log_error(message):
    """
    Log an error message.
    Args:
        message (str): The error message to log.
    """
    logger.error(message)
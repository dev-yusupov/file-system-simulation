import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(message)s", handlers=[logging.StreamHandler()]
)

# Create a logger for the application
logger = logging.getLogger("file_system_simulation")

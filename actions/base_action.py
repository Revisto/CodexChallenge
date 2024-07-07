from log_manager import LogManager
import logging

LogManager.setup_logging()

class Action:
    def __init__(self, driver, parameters):
        self.driver = driver
        self.parameters = parameters

    def execute(self):
        try:
            self.perform_action()
        except Exception as e:
            logging.error(f"Error executing action: {e}")
            # Handle the error as needed, e.g., retry, log, raise a custom exception, etc.

    def perform_action(self):
        raise NotImplementedError("Each action must implement a perform_action method.")
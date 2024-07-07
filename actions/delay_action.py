from .base_action import Action
import time
import logging

class DelayAction(Action):
    def perform_action(self):
        duration = self.parameters['duration']
        logging.info(f"Executing DelayAction for duration: {duration}")
        time.sleep(duration)
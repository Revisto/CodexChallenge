from .base_action import Action
from helium import write, S
import logging

class InputAction(Action):
    def perform_action(self):
        target = self.parameters['target']
        value = self.parameters['value']
        logging.info(f"Executing InputAction on target: {target} with value: {value}")
        write(value, into=S(target))
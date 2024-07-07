from .base_action import Action
from selenium.webdriver.common.action_chains import ActionChains
import logging

class MouseMoveAction(Action):
    def perform_action(self):
        start_position = self.parameters.get('startPosition')
        end_position = self.parameters['endPosition']
        duration = self.parameters.get('duration', 10000)
        logging.info(f"Executing MouseMoveAction from {start_position} to {end_position}")
        action = ActionChains(self.driver, duration=duration)
        if start_position:
            action.move_by_offset(start_position['x'], start_position['y'])
        action.move_by_offset(end_position['x'], end_position['y'])
        action.perform()
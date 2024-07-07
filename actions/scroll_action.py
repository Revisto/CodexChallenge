from helium import scroll_down, scroll_up
import logging

from .base_action import Action

class ScrollAction(Action):
    def perform_action(self):
        direction = self.parameters['direction']
        times = self.parameters['times']  # Number of times to scroll
        logging.info(f"Executing ScrollAction in direction: {direction} for {times} times")
        
        for _ in range(times):
            if direction == "down":
                scroll_down()
            else:
                scroll_up()
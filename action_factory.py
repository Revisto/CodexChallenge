from actions import ClickCSSAction, ClickTextAction, ScrollAction, InputAction, DelayAction, MouseMoveAction
import logging

class ActionFactory:
    @staticmethod
    def get_action(driver, action_data):
        action_type = action_data['type']
        parameters = action_data['parameters']
        logging.info(f"Creating action of type: {action_type} with parameters: {parameters}")
        action_map = {
            'clickCSS': ClickCSSAction,
            'clickText': ClickTextAction,
            'scroll': ScrollAction,
            'input': InputAction,
            'delay': DelayAction,
            'mouseMove': MouseMoveAction
        }
        action_class = action_map.get(action_type)
        if action_class:
            return action_class(driver, parameters)
        else:
            raise ValueError(f"Unsupported action type: {action_type}")
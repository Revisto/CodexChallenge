from .base_action import Action
from helium import click, S
import logging

class ClickCSSAction(Action):
    def perform_action(self):
        target = self.parameters['target']
        logging.info(f"Executing ClickAction on target: {target}")
        click(S(target))

class ClickTextAction(Action):
    def perform_action(self):
        target = self.parameters['target']
        logging.info(f"Executing ClickAction on target: {target}")
        click(target)

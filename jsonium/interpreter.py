# SWAMI KARUPPASWAMI THUNNAI

import json
from .rules.rule import Rule
from .actions.get_action import get_action
from .element import Element
from .variable import Variable

class Interpreter:

    def interpret_rules(self, rules: dict):
        for rule in rules:
            rule_type = rule["type"]
            if rule_type == Rule.ACTION:
                action = get_action(rule["name"])
                action = action(params=rule["params"])
                action.perform()
            elif rule_type == Rule.ELEMENT:
                element = Element(locater=rule["locater"], by=rule["by"])
                Variable.add_variable(rule["var"], element.get_element())


    def interpret_rules_from_file(self, file_path: str):
        with open(file_path, "r") as file:
            rules = json.load(file)
        self.interpret_rules(rules=rules)
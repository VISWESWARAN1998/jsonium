# SWAMI KARUPPASWAMI THUNNAI

import json
from .rules.rule import Rule
from .actions.get_action import get_action
from .element import Element
from .variable import Variable
from .consumer import Consumer
from .memory import Memory

class Interpreter:

    def interpret_rules(self, rules: dict):
        for rule in rules:
            try:
                self.__process_rule(rule=rule)
            except Exception as e:
                if "onerror" in rule:
                    func_name = rule["onerror"]
                    func = Memory.get(name=func_name)
                    func(rule=rule, exception=e)
                else:
                    raise e
    
    def __process_rule(self, rule: dict):
        rule_type = rule["type"]
        if rule_type == Rule.ACTION:
            action = get_action(rule["name"])
            action = action(params=rule["params"])
            action.perform()
        elif rule_type == Rule.ELEMENT:
            element = Element(locater=rule["locater"], by=rule["by"])
            Variable.add_variable(rule["var"], element.get_element())
        elif rule_type == Rule.CONSUMER:
            consumer = Consumer(rule=rule)
            consumer.process_consumer()


    def interpret_rules_from_file(self, file_path: str):
        with open(file_path, "r") as file:
            rules = json.load(file)
        self.interpret_rules(rules=rules)
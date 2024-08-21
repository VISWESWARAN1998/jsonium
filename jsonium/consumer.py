# SWAMI KARUPPASWAMI THUNNAI

from .memory import Memory
from .variable import Variable

class Consumer:

    def __init__(self, rule: dict) -> None:
        self.rule = rule

    def process_consumer(self) -> None:
        func = Memory.get(self.rule["name"])
        params = self.rule["params"]
        func(**{param_name:Variable.get(name=var) for param_name, var in params.items()})
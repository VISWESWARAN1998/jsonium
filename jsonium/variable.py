# SWAMI KARUPPASWAMI THUNNAI

from .globals import VARIABLES


class Variable:
    
    @staticmethod
    def add_variable(name: str, value) -> None:
        global VARIABLES
        VARIABLES[name] = value

    @staticmethod
    def get(name: str):
        global VARIABLES
        return VARIABLES[name]
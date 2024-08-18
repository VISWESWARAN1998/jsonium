# SWAMI KARUPPASWAMI THUNNAI

from .globals import MEMORY


class Memory:
    
    @staticmethod
    def add_memory(name: str, value) -> None:
        global MEMORY
        MEMORY[name] = value

    @staticmethod
    def get(name: str):
        global MEMORY
        print(MEMORY)
        return MEMORY[name]
    
    @staticmethod
    def set_memory(memory: dict) -> None:
        global MEMORY
        MEMORY = memory
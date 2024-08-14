# SWAMI KARUPPASWAMI THUNNAI

class Action:
    """
    The action to be performed on browser/elements
    """

    def __init__(self, name: str, params: dict) -> None:
        self.name = name
        self.params = params

    def get_name(self) -> str:
        return self.name
    
    def get_params(self) -> dict:
        return self.params
    
    def perform(self) -> bool:
        return True
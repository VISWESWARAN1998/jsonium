# SWAMI KARUPPASWAMI THUNNAI

import time
from ..action import Action

class Sleep(Action):

    def __init__(self, name: str = "sleep", params: dict = {}) -> None:
        super().__init__(name, params)

    def perform(self) -> bool:
        time.sleep(self.params["seconds"])
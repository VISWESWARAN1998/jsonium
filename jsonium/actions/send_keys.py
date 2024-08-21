# SWAMI KARUPPASWAMI THUNNAI

import time
from ..action import Action
from ..variable import Variable
from ..params import Params

class SendKeys(Action):

    def __init__(self, name: str = "send_keys", params: dict = {}) -> None:
        super().__init__(name, params)

    def perform(self) -> bool:
        element = Variable.get(self.params["var"])
        element.send_keys(Params(params=self.params).resolve_value_from_memory())
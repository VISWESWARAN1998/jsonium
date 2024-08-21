# SWAMI KARUPPASWAMI THUNNAI

from ..action import Action
from ..variable import Variable
from ..params import Params

class Click(Action):

    def __init__(self, name: str = "click", params: dict = {}) -> None:
        super().__init__(name, params)

    def perform(self) -> bool:
        element = Variable.get(self.params["var"])
        element.click()
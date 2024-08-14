# SWAMI KARUPPASWAMI THUNNAI

from ..action import Action
from ..browser import Browser

class OpenURL(Action):

    def __init__(self, name: str = "open_url", params: dict = {}) -> None:
        super().__init__(name, params)

    def perform(self) -> bool:
        Browser.instance().get(self.params["url"])
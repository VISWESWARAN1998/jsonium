# SWAMI KARUPPASWAMI THUNNAI

from ..action import Action
# Custom actions
from .open_url import OpenURL
from .sleep import Sleep
from .send_keys import SendKeys
from .click import Click
from .wait_until import WaitUntil
# Exceptions
from.exceptions.action_not_found_exception import ActionNotFoundException

SUPPORTED_ACTIONS = [
    OpenURL,
    Sleep,
    SendKeys,
    Click,
    WaitUntil
]

def get_action(name) -> Action:
    for action in SUPPORTED_ACTIONS:
        if action().get_name() == name:
            return action
    raise ActionNotFoundException
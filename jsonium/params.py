# SWAMI KARUPPASWAMI THUNNAI

from .memory import Memory

class Params:
    """
    Used to handle the params present in rule

    #### Example params in rule:
    ```json
    {
        "type": "action",
        "name": "send_keys",
        "params": {"memory": "first_name", "var": "first_name"}
    }
    ```
    """

    def __init__(self, params: dict) -> None:
        self.params = params

    def resolve_value_from_memory(self):
        """
        If memory is available it gets the value from memory else,
        This method looks for the key named `value` which can be used to send
        hard coded strings. 
        """
        return Memory.get(name=self.params["memory"]) if "memory" in self.params else self.params["value"]
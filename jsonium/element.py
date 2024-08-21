# SWAMI KARUPPASWAMI THUNNAI

from selenium.webdriver.common.by import ByType
from selenium.webdriver.remote.webelement import WebElement
from .browser import Browser

class Element:
    """
    #### About
    Denotes the element in a web-page. Example: Buttons, Inputs, Select etc.,

    #### Example Jsonium Rule:
    
    ```json
    {
        "type": "element",
        "locater": "signup_fname",
        "by": "id",
        "var": "first_name"
    }
    ```
    """


    def __init__(self, locater: ByType, by: str) -> None:
        self.locater = locater
        self.by = by

    def get_element(self) -> WebElement:
        """
        Returns the WebElement using jsonium rule
        """
        return Browser.instance().find_element(self.by, self.locater)

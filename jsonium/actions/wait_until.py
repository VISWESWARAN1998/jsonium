# SWAMI KARUPPASWAMI THUNNAI

# Selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Jsonium
from ..browser import Browser
from ..action import Action

class WaitUntil(Action):

    def __init__(self, name: str = "wait_until", params: dict = {}) -> None:
        super().__init__(name, params)

    def perform(self) -> bool:
        seconds = self.params["seconds"]
        by = self.params["by"]
        locator = self.params["locater"]
        poll_frequency = self.params["poll_frequency"] if "poll_frequency" in self.params else 0.5
        wait = WebDriverWait(driver=Browser.instance(), timeout=seconds, poll_frequency=poll_frequency)
        wait.until(
            EC.presence_of_element_located((by, locator))
        )


# SWAMI KARUPPASWAMI THUNNAI

from selenium.webdriver.remote.webdriver import WebDriver
from .globals import BROWSER, MEMORY

class Browser:

    def __init__(self, browser: WebDriver) -> None:
        global BROWSER
        BROWSER = browser

    @staticmethod
    def instance() -> WebDriver:
        return BROWSER
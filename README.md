# Jsonium
Have you ever worked with selenium and felt the need of constantly changing the program just because a selection or xpath is changed? Well, I have came up with a solution on completely automating the selenium using JSON.

The Python code doesn't have to be modified for website changes as we will be completely automating including the logic with JSON. 

The Python code will take the rules from json file named rules.json
```python
# SWAMI KARUPPASWAMI THUNNAI

from selenium import webdriver
from jsonium.browser import Browser
from jsonium.interpreter import Interpreter

browser = Browser(browser=webdriver.Chrome())
interpreter = Interpreter()
interpreter.interpret_rules_from_file(file_path="rules.json")
````


**rules.json:** This rule will open the webiste, wait for 10 sections until an input tag is available and then fills the name.
```json
[
    {
        "type": "action",
        "name": "open_url",
        "params": {"url": "https://ai-being.com"}
    },
    {
        "type": "action",
        "name": "wait_until",
        "params": {"seconds": 10, "by": "xpath", "locater": "/html/body/div/form/input[1]"}
    },
    {
        "type": "element",
        "locater": "/html/body/div/form/input[1]",
        "by": "xpath",
        "var": "first_name"
    },
    {
        "type": "action",
        "name": "send_keys",
        "params": {"value": "Visweswaran", "var": "first_name"}
    }
]
```

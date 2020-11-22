import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary

from src.const import (
    MICROSOFT_EMAIL,
    MICROSOFT_PASSWORD,
    MICROSOFT_LOGIN_URL,
    MICROSOFT_FORM_URL,
    MIN_TEMPERATURE,
    MAX_TEMPERATURE,
    STATE_CONST,
)


def get_temperature():
    return random.randint(MIN_TEMPERATURE, MAX_TEMPERATURE)


class AutoHealthJob:
    TIME_SLEEP = 10
    ACCOUNT_CONTENT_ID = "otherTileText"
    SIGN_IN_TEXT_ID = "i0116"
    SIGN_IN_BUTTON_ID = "idSIButton9"
    SIGN_IN_STATE_ID = "idBtn_Back"
    FORM_TEXT_ID = "office-form-question-textbox office-form-textfield-input form-control office-form-theme-focus-border border-no-radius"
    FORM_RADIO_ID = "office-form-question-choice-row office-form-question-choice-text-row"
    FORM_BUTTON_ID = "button-content"

    def __init__(self, option=False):
        self.state = False
        if option:
            self.options = webdriver.ChromeOptions()
            self.options.add_argument("--headless")
            self.options.add_argument('--disable-gpu')
            self.driver = webdriver.Chrome(options=self.options)
        else:
            self.driver = webdriver.Chrome()

        self.microsoft_login()
        self.run()
        self.driver.quit()

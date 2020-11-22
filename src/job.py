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

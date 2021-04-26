import time
import random
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary

from src.const import (
    MICROSOFT_LOGIN_URL,
    MICROSOFT_FORM_URL,
    MICROSOFT_EMAIL,
    MICROSOFT_PASSWORD,
    MIN_TEMPERATURE,
    MAX_TEMPERATURE,
)


def get_temperature():
    return str(random.uniform(MIN_TEMPERATURE, MAX_TEMPERATURE))[:4]


class AutoHealthJob:
    TIME_SLEEP = 5
    ACCOUNT_CONTENT_ID = "otherTileText"
    SIGN_IN_EMAIL_ID = "i0116"
    SIGN_IN_PASSWORD_ID = "i0118"
    SIGN_IN_BUTTON_ID = "idSIButton9"
    SIGN_IN_STATE_ID = "idBtn_Back"
    FORM_TEXT_ID = '//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div/div/input'
    FORM_2_ID = '//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div/label/input'
    FORM_3_ID = '//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/div[1]/div/label/input'
    FORM_4_ID = '//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[4]/div/div[2]/div/div[2]/div/label/input'
    FORM_BUTTON_ID = '//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[4]/div[1]/button/div'
    MAIL_BUTTON_ID = '//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[3]/div/div/label/input'

    def __init__(self, option=False, attend=True):
        self.state = False
        if option:
            self.options = webdriver.ChromeOptions()
            self.options.add_argument("--headless")
            self.options.add_argument('--disable-gpu')
            self.driver = webdriver.Chrome(options=self.options)
        else:
            self.driver = webdriver.Chrome()

        self.microsoft_login()
        if attend:
            self.run_attend()
        self.driver.find_element(By.XPATH, self.MAIL_BUTTON_ID).click()
        self.driver.find_element(By.XPATH, self.FORM_BUTTON_ID).click()
        self.get_time_sleep()
        self.state = True

        self.get_screen_shot()
        self.driver.quit()

    def get_time_sleep(self):
        print(self.driver.title)
        time.sleep(self.TIME_SLEEP)

    def get_screen_shot(self):
        self.driver.set_window_size(720, 1280)
        width = self.driver.execute_script("return document.body.scrollWidth")
        height = self.driver.execute_script("return document.body.scrollHeight")
        self.driver.set_window_size(width, height)
        self.driver.save_screenshot('screenshot-full.png')

    def microsoft_login(self):
        self.driver.get(MICROSOFT_LOGIN_URL)
        time.sleep(self.TIME_SLEEP)

        # Enter your email address
        element = self.driver.find_element(By.ID, self.SIGN_IN_EMAIL_ID)
        if MICROSOFT_EMAIL is None:
            element.send_keys(os.environ['MICROSOFT_EMAIL'])
        else:
            element.send_keys(MICROSOFT_EMAIL)
        self.driver.find_element(By.ID, self.SIGN_IN_BUTTON_ID).click()
        self.get_time_sleep()

        # Enter your password
        element = self.driver.find_element(By.ID, self.SIGN_IN_PASSWORD_ID)
        if MICROSOFT_PASSWORD is None:
            element.send_keys(os.environ['MICROSOFT_PASSWORD'])
        else:
            element.send_keys(MICROSOFT_PASSWORD)
        self.driver.find_element(By.ID, self.SIGN_IN_BUTTON_ID).click()
        self.get_time_sleep()

    def run_attend(self):
        self.driver.get(MICROSOFT_FORM_URL)
        self.get_time_sleep()

        # Enter your temperature
        element = self.driver.find_element(By.XPATH, self.FORM_TEXT_ID)
        element.send_keys(get_temperature())

        # Select Radio Button
        self.driver.find_element(By.XPATH, self.FORM_2_ID).click()
        self.driver.find_element(By.XPATH, self.FORM_3_ID).click()
        self.driver.find_element(By.XPATH, self.FORM_4_ID).click()

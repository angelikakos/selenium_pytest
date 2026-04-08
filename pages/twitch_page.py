from selenium import webdriver
import logging
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException

logger = logging.getLogger(__name__)


class TwitchPage():
    def __init__(self):
        self.chromeOptions = Options()
        self.chromeOptions.add_argument("--disable-popup-blocking")
        self.chromeOptions.add_argument("--disable-notifications")
        self.chromeOptions.add_argument("--disable-infobars")
        self.chromeOptions.add_experimental_option("mobileEmulation", {
            "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},  # Galaxy S5
            "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"})
        self.driver = webdriver.Chrome(options=self.chromeOptions)

    def goToMainPage(self):
        self.url = "https://m.twitch.tv/"
        self.driver.get(self.url)
        time.sleep(1)
        try:
            self.driver.find_element(By.XPATH, ".//*[contains(.,'Keep using web')]").click()
            self.driver.find_element(By.XPATH, "//button[contains(., 'Accept')]").click()
            logger.info("Twitch webside was found.")
        except (NoSuchElementException, TimeoutException):
            logging.error("No such option.")

    def goSearch(self):
        try:
            self.driver.find_element(By.XPATH, ".//*[text()='Browse']").click()
            time.sleep(3)
            self.button = self.driver.find_element(By.XPATH, "//input['search']")
            self.button.click()
            logger.info("Search option was selected.")
        except (NoSuchElementException, TimeoutException):
            logging.error("No such option.")

    def goToStarCraft(self):
        try:
            self.button.send_keys("StarCraft II")
            self.button.send_keys(Keys.ENTER)
            time.sleep(3)
            logger.info("StarCraft II was selected.")
        except (NoSuchElementException, TimeoutException):
            logging.error("No such option.")

    def scrollTwoTimes(self):
        self.driver.execute_script("window.scrollTo(0, 640)")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(640, 1280)")
        time.sleep(3)

    def open1Streamer(self):
        try:
            self.driver.find_element(By.XPATH, ".//*[text()='CranKy_Ducklings']").click()
            time.sleep(15)
            logger.info("One Stream was selected.")
        except (NoSuchElementException, TimeoutException):
            logging.error("No such option.")
        try:
            self.driver.find_element(By.XPATH, "//*[contains(@class, 'knwRkt')]").click()
            time.sleep(3)
            logger.info("The movie was played.")
        except (NoSuchElementException, TimeoutException):
            logging.info("No such option.")

    def takeScreenShot(self):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        self.driver.save_screenshot(f"screenshot_{timestamp}.png")

    def exit(self):
        self.driver.quit()

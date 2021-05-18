from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from time import sleep


CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
IG_USERNAME = "Your.username@gmail.com"
IG_PASSWORD = "Password"
SIMILAR_ACCOUNT = "Target_account"


class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        sleep(5)
        email = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        email.send_keys(IG_USERNAME)
        password.send_keys(IG_PASSWORD, Keys.ENTER)
        sleep(5)
        skip = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        skip.send_keys(Keys.ENTER)
        sleep(5)
        skip2 = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        skip2.send_keys(Keys.ENTER)
        sleep(5)
    def find_follows(self):

        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        sleep(5)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/'
                                                           'ul/li[2]/a')
        followers.click()

        sleep(3)
        pop_up = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            #scrolling pop-up
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pop_up)
            sleep(3)

    def follow(self):
        # her way
        # all_buttons = self.driver.find_elements_by_css_selector("li button")
        # for button in all_buttons:

        for n in range(1, 500):
            try:
                future_follower = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/'
                                                                    f'ul/div/li[{n}]/div/div[2]/button')
                future_follower.click()
                sleep(1.4)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_button.click()



insta = InstaFollower(CHROME_DRIVER_PATH)
insta.login()
insta.find_follows()
insta.follow()
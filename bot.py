from selenium import webdriver
import os
import time

class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        self.driver = webdriver.Chrome('chromedriver.exe')
        #self.login(username, password)
        self.login()


    def login(self):
        self.driver.get('{}/accounts/login/'.format(self.base_url))
        time.sleep(3)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()

    def nav_user(self, user):
        self.driver.get('{}/{}/'.format(self.base_url, user))

    def follow_user(self, user):
        self.nav_user(user)
        follow_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button')
        follow_button.click()


if __name__ == '__main__':
    ig_bot = InstagramBot('temp_username', 'temp_password')
    #ig_bot.nav_user('martingarrix')
    time.sleep(5)
    ig_bot.follow_user('martingarrix')
    print(ig_bot.username)

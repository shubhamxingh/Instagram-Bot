from selenium import webdriver
import os
import time

class InstagramBot:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        #to automate browser actions (chrome in this case)
        self.driver = webdriver.Chrome('./chromedriver.exe')
        
        self.login()
        
        self.base_url = "https://www.instagram.com/"
        
    
    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        
        self.driver.find_element_by_name('username').send_keys(self.username)
        
        self.driver.find_element_by_name('password').send_keys(self.password)
        
        time.sleep(1)
        #to click on login button
        self.driver.find_element_by_xpath("//div[contains(text(), 'Log In')]").click()
        #Turn on notifications : click on NOT NOW
        time.sleep(2)
        
        #self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]").click()
        
    
    def nav_user(self, user):
        self.driver.get('{}{}'.format(self.base_url, user)) # here {} = self.base_url *which is (www.instagram.com)*
        time.sleep(1)
        
    def follow_user(self, user):
        self.nav_user(user)
        
        self.driver.find_element_by_xpath("//button[contains(text(), 'Follow')]").click()
        
    def unfollow_user(self, user):
        self.nav_user(user)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Following')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]").click()

if __name__ == '__main__':
    
    username = "goodmemeslol"
    password = "9015115792"
    
    ig_bot = InstagramBot(username, password)
    
    ig_bot.unfollow_user('setuptechx')
    
    
    
    
    
    
    
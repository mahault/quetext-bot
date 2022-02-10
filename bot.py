from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import argparse



class Checker():
    def __init__(self):
        
        self.driver = webdriver.Chrome('D:\downloads\chromedriver_win32\chromedriver')
        self.wait = WebDriverWait(self.driver, 90)
        self.driver.get('https://www.quetext.com/login')
        self.username_input = '//*[@id="login_email"]'
        self.pwd_input = '//*[@id="login_password"]'
        self.login_submit_button = '//*[@id="login-container"]/form/div[2]/button'
        self.text_enter = '//*[@id="textarea"]'
        self.text_search = '//*[@id="search"]'

        self.result_container= '//*[@id="doc-details"]'
        self.neg_result = '//*[@id="no-results"]/div/div[2]'
        self.pos_result = '//*[@id="percent-matches"]'

        ## replace with your credentials if you want
        self.username = args.username
        self.pwd = args.pwd

    def login(self):
        # driver.find_element_by_xpath(quetext_search ).click()
        #Login
        self.driver.find_element(By.XPATH, self.username_input).send_keys(self.username)
        self.driver.find_element(By.XPATH, self.pwd_input).send_keys(self.pwd)
        self.driver.find_element(By.XPATH, self.login_submit_button).submit()

    def find_text(self, args):
        #submit text  --- CHOOSE YOUR OWN OR TURN INTO AN ARGSPARSE
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.text_enter))).send_keys(args.string)
        self.driver.find_element(By.XPATH, self.text_search).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.result_container)))
        try:
            not_plagiarised = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.neg_result))).text
            print("not plagiarised",not_plagiarised)
        except:
            plagiarised = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.pos_result))).text
            print("plagiarised", plagiarised)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some string to be verified')
    parser.add_argument('string', type=str, help='a string for the plagiarism checker, 10 words minimum')
    parser.add_argument('username', type=str, help='quetext username')
    parser.add_argument('pwd', type=str, help='quetext pwd')
    args = parser.parse_args()

    checker = Checker()
    checker.login()
    checker.find_text(args)

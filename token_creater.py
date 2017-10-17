#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys
reload(sys)  # Reload is a hack
sys.setdefaultencoding('UTF8')

import smtplib
#import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display
from time import sleep
import marshal


auth_username = ""
auth_password = ""


with Display():

    # we can now start Firefox and it will run inside the virtual display
    driver = webdriver.Firefox()

    try:

        print("Display running...")
        print("Attempting browser...")
        driver = webdriver.Firefox()
        print("Opening browser...")
        url = "https://www.pythonanywhere.com/login"
        driver.get(url)
        wait = WebDriverWait(driver, 30)
        actions = webdriver.ActionChains(driver)

        allowance = wait.until(EC.element_to_be_clickable((By.NAME, "auth-username")))
        # log into marseter account
        loader = wait.until(EC.element_to_be_clickable((By.NAME, "auth-username")))


        loader.click()
        loader.send_keys(auth_username)
        loader = wait.until(EC.element_to_be_clickable((By.NAME, 'auth-password')))
        loader.click()
        loader.send_keys(auth_password)
        loader = wait.until(EC.element_to_be_clickable((By.ID, 'id_next')))
        loader.click()
        sleep(5)

        ##################################################################################
        #change user-account

        driver.get("https://www.pythonanywhere.com/user/Dizziekicks/consoles/")

        cookies = driver.get_cookies()

        with open("cookies.pkl","wb") as ck:
            marshal.dump( cookies , ck )

        print(cookies)

        for cookie in cookies:
            try:
                name = cookie["name"]
                if name == "sessionid":
                    sessionid = cookie["value"]
                if name == "csrftoken":
                    csrftoken = cookie["value"]
            except:
                pass

        cookie = "sessionid="+sessionid+"; __stripe_mid=68f9607e-3ffb-4388-a5fd-206c6c204f14; csrftoken="+csrftoken

        #print(sessionid)
        #print(csrftoken)
        #print(cookie)

        creds = []
        creds.append(cookie)
        creds.append(csrftoken)
        print(creds)

        with open("console_creds.txt","wb") as cc:
            marshal.dump( creds , cc )

    finally:
        driver.quit()


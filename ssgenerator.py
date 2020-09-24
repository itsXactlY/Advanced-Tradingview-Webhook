import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC1
from selenium.webdriver.common.by import By

import config as config
from telegram import Bot
from discord_webhook import DiscordWebhook
import tweepy
import smtplib, ssl
from email.mime.text import MIMEText

telegram = config.send_telegram_alerts
discord  = config.send_discord_alerts

if telegram:
    tg_bot = Bot(token=config.tg_token)

def get_trading_view_graph():

# login
    driver = webdriver.Chrome('chromedriver.exe') # change as per your location
    driver.maximize_window()
    driver.get("https://www.tradingview.com/#signin")
    time.sleep(1)

    id = config.tv_username #input('Enter your Login ID - ')
    password = config.tv_password #input('Enter your Password - ')
    tf = config.tv_timeframe #input('Enter chart timeframe  - ')

    driver.find_element_by_class_name("i-clearfix").click()

    time.sleep(1)
    driver.find_element_by_name("username").send_keys(id)
    time.sleep(1)
    driver.find_element_by_name("password").send_keys(password)
    time.sleep(1)
    driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(2)

    driver.get("https://tradingview.com/chart/qQRu7ERH/")

    time.sleep(2)
    driver.maximize_window()

    ActionChains(driver).key_down(Keys.ALT).send_keys('s').perform()
    wait_time = 25 # a very long wait time

    time.sleep(3)
    

    imageLink = driver.find_element_by_class_name("textInput-3WRWEmm7")
    print(imageLink.get_attribute("value"), driver.current_url)

    tg_bot.sendMessage(config.channel, imageLink.get_attribute("value") )

    return( imageLink.get_attribute("value"), driver.current_url )


if __name__ == '__main__':
    get_trading_view_graph()
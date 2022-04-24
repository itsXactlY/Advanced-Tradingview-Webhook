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

import requests
import os

telegram = config.send_telegram_alerts
discord  = config.send_discord_alerts
twitter  = config.send_twitter_alerts

if telegram:
    tg_bot = Bot(token=config.tg_token)

if twitter:
    tw_auth = tweepy.OAuthHandler(config.tw_ckey, config.tw_csecret)
    tw_auth.set_access_token(config.tw_atoken, config.tw_asecret)
    tw_api = tweepy.API(tw_auth)

def get_trading_view_graph():
#Init Chrome

    driver = webdriver.Chrome('chromedriver.exe') # change as per your location
    driver.maximize_window()
    driver.get("https://www.tradingview.com/#signin")

# login

    id = config.tv_username #input('Enter your Login ID - ')
    password = config.tv_password #input('Enter your Password - ')
    tf = config.tv_timeframe #input('Enter chart timeframe  - ')

    driver.find_element_by_class_name("i-clearfix").click()

    driver.find_element_by_name("username").send_keys(id)

    driver.find_element_by_name("password").send_keys(password)

    driver.find_element_by_xpath("//button[@type='submit']").click()


    driver.get("https://tradingview.com/chart/qQRu7ERH/")

    time.sleep(5)

    ActionChains(driver).key_down(Keys.ALT).send_keys('s').perform()
    wait_time = 25 # a very long wait time
    time.sleep(5)

    imageLink = driver.find_element_by_class_name("text-2FI8ioay")

    print ("Got it! :) %s ", imageLink.get_attribute("value"))

#Post Chart to Telegram 
    
    tg_bot.sendMessage(config.channel, imageLink.get_attribute("value") )

#Post Chart to Discord
    
    discord_alert = DiscordWebhook(url=config.discord_webhook, content=imageLink.get_attribute("value"))
    response = discord_alert.execute()

#Post Chart to Twitter
    
    #Download Chart Image as we can't send images from URL sadly
    request = requests.get(imageLink.get_attribute("value"), stream=True)
    print("to confirm: url: ", imageLink.get_attribute("value"))
    filename = 'temp.jpg'
    message = "Chop that sushi!"

    try:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        tw_api.update_with_media(filename, status=message)
        time.sleep(3) # give some time to upload, just in case...
        os.remove(filename)
    except:
        os.remove(filename)
        print("Unable to download image")

    return( '''imageLink.get_attribute("value"), driver.current_url''' )


if __name__ == '__main__':
    get_trading_view_graph()

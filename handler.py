import config as config
from telegram import Bot
from discord_webhook import DiscordWebhook
import tweepy
import smtplib, ssl
from email.mime.text import MIMEText

##
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC1
from selenium.webdriver.common.by import By


telegram = config.send_telegram_alerts
discord  = config.send_discord_alerts
twitter  = config.send_twitter_alerts
email    = config.send_email_alerts


'''<input class="textInput-3WRWEmm7" readonly="" value="https://www.tradingview.com/x/bVdFutdP/"> '''

def get_trading_view_graph():
    #webDriver.get("https://www.tradingview.com/chart/?symbol=" + exchange +":"+currency)


    driver = webdriver.Chrome('chromedriver.exe') # change as per your location
    driver.get ("https://tradingview.com/chart/qQRu7ERH/")
    
    # options = webdriver.ChromeOptions() 
    # options.add_argument("download.default_directory=C:\py-webhook")
    
    driver.maximize_window()

    ActionChains(driver).key_down(Keys.ALT).send_keys('s').perform()
    screenshotbutton = driver.find_element_by_class_name("Copy")
    screenshotbutton.click()
    time.sleep(3)
    
    
    
    # imageLink = driver.find_element_by_class_name("Copy")
    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        print(elem.get_attribute("href"))

    
    
    
    
    tg_bot.sendMessage(config.channel, imageLink.get_attribute("value"), driver.current_url )
    return( imageLink.get_attribute("value"), driver.current_url )








def scrapeChart():
    driver = webdriver.Chrome('chromedriver.exe') # change as per your location
    driver.get ("https://tradingview.com/chart/qQRu7ERH/")
    
    # options = webdriver.ChromeOptions() 
    # options.add_argument("download.default_directory=C:\py-webhook")
    
    driver.maximize_window()

    ActionChains(driver).key_down(Keys.ALT).send_keys('s').perform()
    wait_time = 25 # a very long wait time
    element = WebDriverWait(driver, wait_time).until(EC1.element_to_be_clickable((By.LINK_TEXT, 'Copy')))#'Save image')))
    element.click()
    time.sleep(3)
    driver.close()
















if telegram:
    tg_bot = Bot(token=config.tg_token)

if twitter:
    tw_auth = tweepy.OAuthHandler(config.tw_ckey, config.tw_csecret)
    tw_auth.set_access_token(config.tw_atoken, config.tw_asecret)
    tw_api = tweepy.API(tw_auth)
    
def send_buy_order(data):
    if telegram:
        tg_bot.sendMessage(config.channel, data)
        get_trading_view_graph()
        print('Alert has been sent to Telegram.')

    else:
        print('INFO: Telegram alerts are disabled.')
        
    if discord:
        discord_alert = DiscordWebhook(url=config.discord_webhook, content=data)
        response = discord_alert.execute()
        print('Alert has been sent to Discord.')
    else:
        print('INFO: Discord alerts are disabled.')
        
    if twitter:
        tw_api.update_status(status=data)
        print('Alert has been sent to Twitter.')
    else:
        print('INFO: Twitter alerts are disabled.')
        
    if email:
        email_msg = MIMEText(data)
        email_msg['Subject'] = config.email_subject
        email_msg['From']    = config.email_sender
        email_msg['To']      = config.email_sender
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(config.email_host, config.email_port, context=context) as server:
            server.login(config.email_user, config.email_password)
            server.sendmail(config.email_sender, config.email_receivers, email_msg.as_string())
            server.quit()
            print('Alert has been sent by email.')
    else:
        print('INFO: Email alerts are disabled.')
  
def send_sell_order(data): 
    if telegram:
        tg_bot.sendMessage(config.channel, data)
        print('Alert has been sent to Telegram.')
    else:
        print('INFO: Telegram alerts are disabled.')
        
    if discord:
        discord_alert = DiscordWebhook(url=config.discord_webhook, content=data)
        response = discord_alert.execute()
        print('Alert has been sent to Discord.')
    else:
        print('INFO: Discord alerts are disabled.')
        
    if twitter:
        tw_api.update_status(status=data)
        print('Alert has been sent to Twitter.')
    else:
        print('INFO: Twitter alerts are disabled.')
        
    if email:
        email_msg = MIMEText(data)
        email_msg['Subject'] = config.email_subject
        email_msg['From']    = config.email_sender
        email_msg['To']      = config.email_sender
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(config.email_host, config.email_port, context=context) as server:
            server.login(config.email_user, config.email_password)
            server.sendmail(config.email_sender, config.email_receivers, email_msg.as_string())
            server.quit()
            print('Alert has been sent by email.')
    else:
        print('INFO: Email alerts are disabled.')
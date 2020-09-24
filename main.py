import config as config
from flask import Flask, request, abort
from handler import send_buy_order, send_sell_order

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC1
from selenium.webdriver.common.by import By


app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = request.get_data(as_text=True)
        if config.Buy_Alert in data:
            print('Alert Received:', data)
            send_buy_order(data)
            #scrapeChart()
            return '', 200
        elif config.Sell_Alert in data:
            print('Alert Received:', data)
            send_sell_order(data)
            return '', 200
        else:
            abort(400)
    else:
        abort(400)


if __name__ == '__main__':

    from waitress import serve
    serve(app, host='0.0.0.0', port=80)
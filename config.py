# Alert message in TradingView (ex. https://i.imgur.com/RFkuf1d.png)
Buy_Alert  = ''
Sell_Alert = ''

# Telegram Settings
send_telegram_alerts = True
tg_token   = '' # Bot token. Get it from @Botfather
channel    = '-100'   # Channel ID (ex. -1001487568087) aLca :: Note: -100 is important as start

# Discord Settings
send_discord_alerts = False
discord_webhook     = 'https://discordapp.com/api/webhooks/-??? :)'    # Discord Webhook URL (https://support.discordapp.com/hc/de/articles/228383668-Webhooks-verwenden)

#Twitter Settings
send_twitter_alerts = False
tw_ckey    = ''
tw_csecret = ''
tw_atoken  = ''
tw_asecret = ''

# Email Settings
send_email_alerts = False
email_sender      = ''        # Your email address
email_receivers   = ['', '']  # Receivers, can be multiple
email_subject     = 'i bims, just a test'

email_port     = 465    # SMTP SSL Port (ex. 465)
email_host     = ''     # SMTP host (ex. smtp.gmail.com)
email_user     = ''     # SMTP Login credentials
email_password = ''     # SMTP Login credentials



# TradingView Login to get Realtime Charts

tv_username = ''
tv_password = ''
tv_timeframe = '1H' # obsolete, todo: delete me and clean code up
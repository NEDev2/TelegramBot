import telebot
import os
from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
#chrome_options.add_argument("--headless")

chat_id = 2129581818

url_1 = "https://docs.google.com/presentation/d/e/2PACX-1vTMhqj6mlS1m3kr6GBjqVV3FuJQB8WJzjOn4jflYXGxE_oK3J3nE3fxpHyafEC4v5f5El0QVIiJwxCK/embed?start=false&loop=false&delayms=5000#slide=id.ge88f06493c_0_253"
url_2 = "https://docs.google.com/presentation/d/e/2PACX-1vQexuBLnbGAApTO-V42ie_7i9zUXbhA8CxqIxT4FXdqv-EzMQLrEJOeAsPnwNpWk-GFOSSOoC6pfvby/embed?start=false&loop=false&delayms=5000#slide=id.ge88f06493c_0_253"
url_3 = "https://docs.google.com/presentation/d/e/2PACX-1vTTlLqShyUclyJhqjkx-DNSJUEXZ705BURkXJRv4r_RCA_L8NIq78NLarVkcJDjkY0-wg0pGwwtL7v4/embed?start=false&loop=false&delayms=5000#slide=id.ge88f06493c_0_253"
url_4 = "https://docs.google.com/presentation/d/e/2PACX-1vTekbddzGCNADWrkYquZW_3bSCKCzc-_4C2Pakz2iG4rhoK0G_ABLf5Qx2TM2zKF6kAjnEN5Bdn9XeX/embed?start=false&loop=false&delayms=5000#slide=id.gf19c7cd623_0_1"
url_5 = "https://docs.google.com/presentation/d/e/2PACX-1vTSJqI9F6QVNevkCTt8imccvQhXCzkkKsF3d76nfBn0dDa_srIFyLCMkb9hlo4wq9VuCOHICEC53NqB/embed?start=false&loop=false&delayms=5000#slide=id.ge88f06493c_0_253"


def send_message():
    driver = webdriver.Chrome(options=chrome_options)

    day = datetime.today().weekday()
    print(day)

    if day == 7:
      pass

    url = ""
    if day == 0:
        url = url_3
    if day == 1:
        url = url_4
    if day == 2:
        url = url_5
    if day == 3:
        url = url_1
    if day == 5:
        url = url_1
    if day == 6:
        url = url_1

    if url == "":
        pass

    driver.get(url)

    sleep(0.4)
    driver.set_window_size(1500, 1500)

    sleep(0.1)
    driver.save_screenshot('photo.png')

    sleep(0.1)
    bot.send_photo(chat_id, open("photo.png", "rb"))

    print("Sent photo!")
    sleep(0.5)
    driver.quit()
    os.remove("photo.png")


API_KEY = os.environ['API']
bot = telebot.TeleBot(API_KEY)

while True:

    send_message()
    sleep(60 * 60 * 7)
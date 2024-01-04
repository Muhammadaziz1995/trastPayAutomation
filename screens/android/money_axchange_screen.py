from screens.screen import Screen
from selenium.common import NoSuchElementException
import time


class MoneyExchangeScreen(Screen):
    money_exchange_screen_title = ("xpath", "//*[@text='Konversiya']")

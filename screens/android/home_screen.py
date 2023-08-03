from screens.screen import Screen
from selenium.common import NoSuchElementException
import time


class HomeScreen(Screen):

    profile_owner_name = ("id", "trastpay.uz:id/textViewName")

    def is_home_screen_open(self):
        try:
            if "MUHAMMADAZIZ" in self.get_element_text(self.profile_owner_name):
                return True
        except Exception:
            raise NoSuchElementException
        return False

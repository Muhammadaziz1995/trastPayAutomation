from screens.screen import Screen
from selenium.common import NoSuchElementException
import time


class WelcomeScreen(Screen):
    screen_title = ("id", "trastpay.uz:id/textViewWellCome")
    language_dropdown = ("id", "trastpay.uz:id/layoutLanguage")
    phone_number_field = ("id", "trastpay.uz:id/phone")
    lang_uzb = ("id", "trastpay.uz:id/textViewUz")
    dear_user_message = ("id", "trastpay.uz:id/textViewTitle")

    """ ** Kirish screen ** """
    kirish_screen_title = ("id", "trastpay.uz:id/textViewWellCome")
    phone_number_container = ("id", "trastpay.uz:id/textViewPhoneNumber")
    password_input_field = ("id", "trastpay.uz:id/password")
    davom_etish_button = ("id", "trastpay.uz:id/btnContinue")
    """ ** Kirish screen ends ** """

    """ ** OTP Tasdiqlash screen ** """
    tasdiqlash_screen_title = ("id", "trastpay.uz:id/textViewWellCome")
    otp_input_field = ("id", "trastpay.uz:id/edittext1")
    phone_number_container_in_otp_screen = ("id", "trastpay.uz:id/textViewPhoneNumber")
    """ ** OTP Tasdiqlash screen ends ** """

    """ ** PIN code screen ** """
    pin_code_screen_title = ("id", "trastpay.uz:id/textViewTitle")
    confirm_pin_code_screen_title = ("id", "trastpay.uz:id/textViewTitle")
    button_5 = ("id", "trastpay.uz:id/button5")
    button_7 = ("id", "trastpay.uz:id/button7")
    button_0 = ("id", "trastpay.uz:id/button0")
    """ ** PIN code screen ends ** """

    def is_welcome_screen_open(self):
        try:
            if self.is_visible(self.screen_title):
                return True
        except Exception:
            raise NoSuchElementException
        return False

    def is_kirish_screen_open(self):
        try:
            if self.is_visible(self.kirish_screen_title):
                return True
        except Exception:
            raise NoSuchElementException
        return False

    def is_confirm_pin_code_screen_open(self):
        if "PIN kodni tasdiqlang" in self.get_element_text(self.confirm_pin_code_screen_title):
            return True
        return False

    def is_pin_code_screen_open(self):
        if "PIN kodni oʻrnating" in self.get_element_text(self.confirm_pin_code_screen_title):
            return True
        return False

    def is_enter_pin_code_screen_open(self):
        if "PIN kodni kiriting" in self.get_element_text(self.pin_code_screen_title):
            return True
        return False

    def is_otp_tasdiqlash_screen_open(self):
        if self.is_visible(self.tasdiqlash_screen_title):
            return True
        return False

    def is_entered_phone_number_exist(self, phone_num):
        if phone_num in self.get_element_text(self.phone_number_container_in_otp_screen):
            return True
        return False

    def is_dear_user_message_appear(self):
        if "Hurmatli MUHAMMADAZIZ!" in self.get_element_text(self.dear_user_message):
            return True
        return False

    def enter_password(self, password):
        self.enter_data(self.password_input_field, password)

    def enter_phone_numb(self, phone_number):
        self.enter_data(self.phone_number_field, phone_number)

    def change_lang_to_uzb(self):
        self.click(self.language_dropdown)
        self.click(self.lang_uzb)

    def click_on_davom_etish_button(self):
        self.click(self.davom_etish_button)

    def create_pin_code(self):
        numbers = [self.button_5, self.button_7, self.button_0, self.button_7]
        for number in numbers:
            self.click(number)


import allure
from allure_commons.types import AttachmentType

from flows.android.android_base_flow import AndroidBaseFlow
import time


class LoginFlow(AndroidBaseFlow):
    def __init__(self, driver, app_path):
        super().__init__(driver, app_path)
        self.driver = driver

    def check_login(self, phone_number, password):
        assert self.install_application(True)
        self.welcome_screen.change_lang_to_uzb()
        assert self.welcome_screen.is_welcome_screen_open()
        self.welcome_screen.enter_phone_numb(phone_number)
        assert self.welcome_screen.is_kirish_screen_open()
        self.welcome_screen.enter_password(password)
        self.welcome_screen.click_on_davom_etish_button()
        assert self.welcome_screen.is_otp_tasdiqlash_screen_open()
        self.p2p_screen.enter_otp('998112')
        # assert self.welcome_screen.is_entered_phone_number_exist(phone_number)
        time.sleep(1)
        assert self.welcome_screen.is_pin_code_screen_open()
        self.welcome_screen.create_pin_code()
        assert self.welcome_screen.is_confirm_pin_code_screen_open()
        self.welcome_screen.create_pin_code()
        assert self.welcome_screen.is_dear_user_message_appear()
        time.sleep(2)
        return True

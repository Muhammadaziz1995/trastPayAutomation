from allure_commons.types import AttachmentType

from flows.android.android_base_flow import AndroidBaseFlow
import time
import allure


class ProfileFlow(AndroidBaseFlow):
    def __init__(self, driver, app_path):
        super().__init__(driver, app_path)
        self.driver = driver

    def check_app_lock_time(self):
        assert self.install_application(False)
        self.welcome_screen.is_enter_pin_code_screen_open()
        self.welcome_screen.create_pin_code()
        assert self.home_screen.is_home_screen_open()
        self.home_screen.click_on_profile_icon()
        assert self.home_screen.is_profile_screen_open()
        self.home_screen.click_on_security_option()
        assert self.home_screen.is_security_screen_open()
        self.home_screen.select_time_to_lock_app()
        time_lim = self.home_screen.get_time_limit_for_lock()
        self.home_screen.click_on_back_arrow()
        self.home_screen.click_on_back_arrow()
        self.home_screen.click_on_home_button()
        time.sleep(time_lim + 1)
        self.home_screen.scroll_to_open_apps()
        self.home_screen.click_on_trastpay_app()
        self.welcome_screen.is_enter_pin_code_screen_open()
        self.welcome_screen.create_pin_code()
        assert self.home_screen.is_home_screen_open()
        return True




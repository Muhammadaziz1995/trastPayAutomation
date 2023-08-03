from tests.utils import lazy_property
from conftest import PATH
from navigations.android.navigation import NavigationAndroid
from screens.android.welcome_screen import WelcomeScreen
from screens.android.home_screen import HomeScreen
from screens.android.p2p_screen import P2PScreen
from screens.android.cheque_screen import ChequeScreen


class AndroidBaseFlow:
    def __init__(self, driver, app_path):
        self.driver = driver
        self.app_path = app_path

    def install_application(self, login=True):
        if login:
            self.driver.remove_app('trastpay.uz')
            self.driver.install_app(PATH(self.app_path))
            self.driver.launch_app()
            return True
        else:
            self.driver.install_app(PATH(self.app_path))
            self.driver.launch_app()
            return True

    @lazy_property
    def welcome_screen(self):
        return WelcomeScreen(self.driver)

    @lazy_property
    def navigation(self):
        return NavigationAndroid(self)

    @lazy_property
    def home_screen(self):
        return HomeScreen(self.driver)

    @lazy_property
    def p2p_screen(self):
        return P2PScreen(self.driver)

    @lazy_property
    def cheque_screen(self):
        return ChequeScreen(self.driver)
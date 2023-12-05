from tests.utils import lazy_property
from conftest import PATH
# from navigations.android.navigation import NavigationAndroid
from screens.android.welcome_screen import WelcomeScreen
from screens.android.home_screen import HomeScreen
from screens.android.p2p_screen import P2PScreen
from screens.android.cheque_screen import ChequeScreen
from screens.android.payments_screen import PaymentsScreen
from screens.android.loan_screen import LoanScreen
from screens.android.money_axchange_screen import MoneyExchangeScreen
from screens.screen import Screen


class AndroidBaseFlow:
    def __init__(self, driver, app_path):
        self.driver = driver
        self.app_path = app_path

    def install_application(self, login=True):
        if login:
            self.driver.remove_app('trastpay.uz')
            self.driver.install_app(PATH(self.app_path))
            self.driver.activate_app('trastpay.uz')
            return True
        else:
            self.driver.install_app(PATH(self.app_path))
            self.driver.activate_app('trastpay.uz')
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

    @lazy_property
    def payments_screen(self):
        return PaymentsScreen(self.driver)

    @lazy_property
    def loan_screen(self):
        return LoanScreen(self.driver)


    @lazy_property
    def money_exchange_screen(self):
        return MoneyExchangeScreen(self.driver)


    @lazy_property
    def screens(self):
        return Screen(self.driver)
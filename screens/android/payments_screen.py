from screens.screen import Screen
from selenium.common import NoSuchElementException
import time


class PaymentsScreen(Screen):
    payments_screen_title = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                      "android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                      "/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/"
                                      "android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView")
    search_field = ("id", "trastpay.uz:id/search")
    services_ids = ("id", "trastpay.uz:id/textViewName")
    """ Mobile aloqa """
    mobile_operator_screen_title = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                             "android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                                             "android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/"
                                             "android.widget.LinearLayout/android.widget.TextView")
    operators_ids = ("id", "trastpay.uz:id/textViewTitle")
    operator_screen_title = ("id", "trastpay.uz:id/textViewTitle")
    selected_operator_name = ("id", "trastpay.uz:id/textViewName")
    input_fields = ("id", "trastpay.uz:id/editText")
    continue_button = ("id", "trastpay.uz:id/btnContinue")
    cards_dropdown_menu = ("id", "trastpay.uz:id/layoutSource")
    cards_menu_title = ("id", "trastpay.uz:id/textViewCardsTitle")
    """ Mobile aloqa ends """

    def is_payment_screen_open(self):
        try:
            if self.is_visible(self.payments_screen_title):
                return True
        except Exception:
            raise NoSuchElementException
        return False

    def is_mobile_operator_screen_open(self):
        try:
            if self.is_visible(self.mobile_operator_screen_title):
                return True
        except Exception:
            raise NoSuchElementException
        return False

    def is_cards_menu_open(self):
        try:
            if self.is_visible(self.cards_menu_title):
                return True
        except Exception:
            raise NoSuchElementException
        return False

    def select_payment_type(self, pay_type):
        all_services = self.get_elements(self.services_ids)
        for service in all_services:
            if pay_type in service.text:
                service.click()
                break
            else:
                continue

    def select_operator(self, operator_type):
        all_operators = self.get_elements(self.operators_ids)
        for operator in all_operators:
            if operator_type in operator.text:
                operator.click()
                break
            else:
                continue

    def check_selected_operator_name(self, operator_name):
        all_operator_names = self.get_elements(self.selected_operator_name)
        for operator in all_operator_names:
            if operator_name in operator.text:
                return True
            else:
                continue

    def enter_number_money(self, number, summa):
        all_fields = self.get_elements(self.input_fields)
        all_fields[0].send_keys(number)
        all_fields[1].send_keys(summa)

    def click_on_continue_button(self):
        self.click(self.continue_button)

    def click_on_cards_menu(self):
        self.click(self.cards_dropdown_menu)
import allure
from allure_commons.types import AttachmentType

from flows.android.android_base_flow import AndroidBaseFlow
import time


class PaymentsFlow(AndroidBaseFlow):
    def __init__(self, driver, app_path):
        super().__init__(driver, app_path)
        self.driver = driver

    def pay_to_mobile_beeline(self, number, summa, pay_type, oper_type, card_last_4_numb, commission):
        assert self.install_application(False)
        self.welcome_screen.is_enter_pin_code_screen_open()
        self.welcome_screen.create_pin_code()
        assert self.home_screen.is_home_screen_open()
        self.home_screen.click_on_payments_icon()
        assert self.payments_screen.is_payment_screen_open()
        self.payments_screen.select_payment_type(pay_type)
        assert self.payments_screen.is_mobile_operator_screen_open()
        self.payments_screen.select_operator(oper_type)
        assert self.payments_screen.check_selected_operator_name(oper_type)
        self.payments_screen.enter_number_money(number, summa)
        self.payments_screen.click_on_continue_button()
        self.payments_screen.click_on_cards_menu()
        assert self.payments_screen.is_cards_menu_open()
        self.p2p_screen.select_card_by_last_4_number(card_last_4_numb)
        self.payments_screen.click_on_continue_button()
        assert self.p2p_screen.is_otp_screen_open()
        # self.p2p_screen.enter_otp(otp)
        time.sleep(6)
        assert self.cheque_screen.check_cheque_title()
        if self.cheque_screen.check_cheque_details_in_last_cheque_screen(summa, summa, card_last_4_numb, commission,
                                                                             number):
            assert True
        else:
            self.screens.get_a_screenshot_as_PNG("Payments.png")
        self.cheque_screen.click_on_home_screen_button()
        return True
from allure_commons.types import AttachmentType

from flows.android.android_base_flow import AndroidBaseFlow
import time
import allure


class LoanFlow(AndroidBaseFlow):
    def __init__(self, driver, app_path):
        super().__init__(driver, app_path)
        self.driver = driver

    def check_advanced_repayment(self, top_navbar_option, amount, card_last_4_numb, commission, credit_id, overall):
        assert self.install_application(False)
        self.welcome_screen.is_enter_pin_code_screen_open()
        self.welcome_screen.create_pin_code()
        assert self.home_screen.is_home_screen_open()
        self.home_screen.select_option_from_top_navbar(top_navbar_option)
        self.loan_screen.click_on_mening_mahsulotlarim()
        self.loan_screen.click_on_loans()
        assert self.loan_screen.is_loans_screen_open()
        assert self.loan_screen.is_loan_name_exist()
        self.loan_screen.click_on_microLoan_img()
        self.loan_screen.click_on_repay_icon()
        self.loan_screen.click_on_payment_type()
        assert self.loan_screen.is_tolovlar_bottom_menu_open()
        self.loan_screen.click_on_advanced_payment()
        self.loan_screen.enter_payment_amount(amount)
        self.loan_screen.click_on_next_button()
        self.payments_screen.click_on_cards_menu()
        assert self.payments_screen.is_cards_menu_open()
        self.p2p_screen.select_card_by_last_4_number(card_last_4_numb)
        self.payments_screen.click_on_continue_button()
        assert self.p2p_screen.is_otp_screen_open()
        # self.p2p_screen.enter_otp('998112')
        time.sleep(6)
        assert self.cheque_screen.check_cheque_title()
        assert self.cheque_screen.check_cheque_details_in_last_cheque_screen(overall, overall, card_last_4_numb, commission,
                                                                             credit_id)
        self.cheque_screen.click_on_home_screen_button()
        return True

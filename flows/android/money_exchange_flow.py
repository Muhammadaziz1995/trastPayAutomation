from flows.android.android_base_flow import AndroidBaseFlow
import time


class MoneyExchangeFlow(AndroidBaseFlow):
    def __init__(self, driver, app_path):
        super().__init__(driver, app_path)
        self.driver = driver

    # def check_money_exchange_from_uzs_to_usd_visa(self, recipient_card_last_4_numb, currency):
    #     assert self.install_application(False)
    #     self.welcome_screen.is_enter_pin_code_screen_open()
    #     self.welcome_screen.create_pin_code()
    #     assert self.home_screen.is_home_screen_open()
    #     self.home_screen.click_on_money_exchange_on_home_screen()
    #     assert self.money_exchange_screen.is_money_exchange_screen_title_exist()
    #     self.money_exchange_screen.click_on_recipient_part()
    #     assert self.money_exchange_screen.is_manbani_tanlang_opened()
    #     self.money_exchange_screen.click_on_recipient_card_number(recipient_card_last_4_numb)
    #     assert self.money_exchange_screen.is_selected_card_info_appear(recipient_card_last_4_numb)
    #     assert self.money_exchange_screen.is_recipient_account_USD_exists()
    #     sent_sum = self.money_exchange_screen.get_current_usd_rate_text_for_cheque()
    #     print("Sent Sum amount: ", sent_sum)
    #     self.money_exchange_screen.enter_money_amount(currency)
    #     # assert self.money_exchange_screen.is_final_usd_amount_exist()
    #     self.money_exchange_screen.click_on_send_btn()
    #     assert self.money_exchange_screen.is_confirm_screen_open()
    #     self.money_exchange_screen.click_on_send_btn()
    #     assert self.p2p_screen.is_otp_screen_open()
    #     time.sleep(6)
    #     commission = '0'
    #     sender_card = self.money_exchange_screen.get_sender_card_last_4_num()
    #     assert self.cheque_screen.check_cheque_title()
    #     assert self.cheque_screen.check_cheque_details_in_last_cheque_screen(sent_sum, sent_sum, sender_card, commission,
    #                                                recipient_card_last_4_numb)
    #     return True

    def check_money_exchange_from_usd_to_uzs_visa(self, recipient_card_last_4_numb, currency):
        assert self.install_application(False)
        self.welcome_screen.is_enter_pin_code_screen_open()
        self.welcome_screen.create_pin_code()
        assert self.home_screen.is_home_screen_open()
        self.home_screen.click_on_money_exchange_on_home_screen()
        assert self.money_exchange_screen.is_money_exchange_screen_title_exist()
        self.money_exchange_screen.click_on_recipient_part()
        assert self.money_exchange_screen.is_manbani_tanlang_opened()
        self.money_exchange_screen.click_on_recipient_card_number(recipient_card_last_4_numb)
        self.money_exchange_screen.click_on_swipe_icon()
        assert self.money_exchange_screen.is_selected_card_info_appear('5309')
        assert self.money_exchange_screen.is_recipient_account_USD_exists()
        self.money_exchange_screen.enter_money_amount(currency)
        assert self.money_exchange_screen.is_final_usd_amount_exist()
        self.money_exchange_screen.click_on_send_btn()
        assert self.money_exchange_screen.is_confirm_screen_open()
        self.money_exchange_screen.click_on_send_btn()
        assert self.p2p_screen.is_otp_screen_open()
        time.sleep(6)
        sent_sum = '1'
        commission = '0'
        sender_card = '5309'
        assert self.cheque_screen.check_cheque_title()
        assert self.cheque_screen.check_cheque_details_in_last_cheque_screen(sent_sum, sent_sum, sender_card,
                                                                             commission, recipient_card_last_4_numb)
        return True

    def check_money_exchange_from_uzs_to_usd_master(self):
        pass

    def check_money_transfer_from_usd_to_uzs_master(self):
        pass
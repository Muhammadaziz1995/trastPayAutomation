from flows.android.android_base_flow import AndroidBaseFlow
import time


class P2PFlow(AndroidBaseFlow):
    def __init__(self, driver, app_path):
        super().__init__(driver, app_path)
        self.driver = driver

    def check_p2p_humo_to_humo_from_home_screen(self, sender_card_last_four_numb, recipient_card_numb, sent_money,
                                                recipient_card_4_numb, recipient_full_name):
        assert self.install_application(False)
        self.welcome_screen.is_enter_pin_code_screen_open()
        self.welcome_screen.create_pin_code()
        assert self.home_screen.is_home_screen_open()
        self.p2p_screen.click_on_transfer_to_card_icon_in_home()
        self.p2p_screen.click_on_sender_part()
        self.p2p_screen.select_card_by_last_4_number(sender_card_last_four_numb) #0118
        self.p2p_screen.enter_recipient_card_number(recipient_card_numb) #9860200101864805
        assert self.p2p_screen.check_recipient_name_appeared_after_passing_card_number(recipient_full_name)
        self.p2p_screen.enter_money_for_transferring(sent_money)
        time.sleep(2)
        commission = self.p2p_screen.get_appeared_commission_amount()
        overall_amount = self.p2p_screen.get_appeared_overall_amount(commission)
        print("Overall amount : ", overall_amount)
        self.p2p_screen.click_on_otkazish_button()
        assert self.p2p_screen.is_confirm_transfer_screen_title()
        assert self.p2p_screen.check_all_data_appear_in_confirm_screen(recipient_card_4_numb, sent_money, commission,
                                                                       overall_amount)
        self.p2p_screen.click_on_otkazish_button()
        assert self.p2p_screen.is_otp_screen_open()
        # self.p2p_screen.enter_otp(otp)
        time.sleep(6)
        assert self.cheque_screen.check_cheque_title()
        assert self.cheque_screen.check_cheque_details_in_last_cheque_screen(overall_amount, sent_money, sender_card_last_four_numb,
                                                                             commission, recipient_full_name)
        return True

    def check_p2p_humo_to_uzcard(self, sender_card_last_four_numb, recipient_card_numb, sent_money,
                                                recipient_card_4_numb, recipient_full_name):
        assert self.install_application(False)
        self.welcome_screen.is_enter_pin_code_screen_open()
        self.welcome_screen.create_pin_code()
        assert self.home_screen.is_home_screen_open()
        self.p2p_screen.click_on_transfer_to_card_icon_in_home()
        self.p2p_screen.click_on_sender_part()
        self.p2p_screen.select_card_by_last_4_number(sender_card_last_four_numb)  # 0118
        self.p2p_screen.enter_recipient_card_number(recipient_card_numb)  # 8600140255564529
        assert self.p2p_screen.check_recipient_name_appeared_after_passing_card_number(recipient_full_name)
        self.p2p_screen.enter_money_for_transferring(sent_money)
        time.sleep(2)
        commission = self.p2p_screen.get_appeared_commission_amount()
        overall_amount = self.p2p_screen.get_appeared_overall_amount(commission)
        self.p2p_screen.click_on_otkazish_button()
        assert self.p2p_screen.is_confirm_transfer_screen_title()
        assert self.p2p_screen.check_all_data_appear_in_confirm_screen(recipient_full_name, sent_money, commission,
                                                                       overall_amount)
        self.p2p_screen.click_on_otkazish_button()
        assert self.p2p_screen.is_otp_screen_open()
        # self.p2p_screen.enter_otp(otp)
        time.sleep(6)
        assert self.cheque_screen.check_cheque_title()
        assert self.cheque_screen.check_cheque_details_in_last_cheque_screen(overall_amount, sent_money,
                                                                             sender_card_last_four_numb,
                                                                             commission, recipient_full_name)
        return True

    def check_p2p_humo_to_wallet(self, sender_card_last_four_numb, sent_money, recipient_fullname):
        assert self.install_application(False)
        self.welcome_screen.is_enter_pin_code_screen_open()
        self.welcome_screen.create_pin_code()
        assert self.home_screen.is_home_screen_open()
        self.p2p_screen.click_on_transfer_to_my_funds_in_home()
        self.p2p_screen.click_on_sender_part()
        self.p2p_screen.select_card_by_last_4_number(sender_card_last_four_numb)  # 0118
        self.p2p_screen.click_on_recipient_part()
        self.p2p_screen.scroll_to_wallet()
        self.p2p_screen.select_card_by_title("Cashback hamyon")
        assert self.p2p_screen.check_recipient_name_appeared_after_passing_card_number("Cashback hamyon")
        self.p2p_screen.enter_money_for_transferring(sent_money)
        time.sleep(2)
        commission = self.p2p_screen.get_appeared_commission_amount()
        overall_amount = self.p2p_screen.get_appeared_overall_amount(commission)
        self.p2p_screen.click_on_otkazish_button()
        assert self.p2p_screen.is_confirm_transfer_screen_title()
        assert self.p2p_screen.check_all_data_appear_in_confirm_screen(recipient_fullname, sent_money, commission,
                                                                       overall_amount)
        self.p2p_screen.click_on_otkazish_button()
        assert self.p2p_screen.is_otp_screen_open()
        # self.p2p_screen.enter_otp(otp)
        time.sleep(6)
        assert self.cheque_screen.check_cheque_title()
        assert self.cheque_screen.check_cheque_details_in_last_cheque_screen(overall_amount, sent_money,
                                                                             sender_card_last_four_numb,
                                                                             commission, recipient_fullname)
        return True

    def check_p2p_humo_to_master(self):
        pass

    def check_p2p_uzcard_to_uzcard(self):
        pass

    def check_p2p_uzcard_to_humo(self):
        pass

    def check_p2p_uzcard_to_wallet(self):
        pass

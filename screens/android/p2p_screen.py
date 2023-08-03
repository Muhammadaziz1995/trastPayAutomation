from screens.screen import Screen
from selenium.common import NoSuchElementException
import time


class P2PScreen(Screen):

    transfer_to_card_in_home_screen = ("id", "trastpay.uz:id/imageViewSmallOne")
    transfer_screen_title = ("id", "trastpay.uz:id/editTextCardNumber")
    confirmation_screen_title = ("id", "trastpay.uz:id/textViewName")
    sender_part = ("id", "trastpay.uz:id/viewSender")
    recipient_from_history_icon = ("id", "trastpay.uz:id/imageViewReceiverSelect")
    recipient_card_input_field = ("id", "trastpay.uz:id/editTextCardNumber")
    money_amount_input_field = ("id", "trastpay.uz:id/editTextAmount")
    cards_number_ids = ("id", "trastpay.uz:id/textViewDesc")
    recipient_full_name_on_card = ("id", "trastpay.uz:id/textViewDescReceiver")
    otkazish_button = ("id", "trastpay.uz:id/btnContinue")
    recipient_card_details_in_confirmation_screen = ("id", "trastpay.uz:id/textViewRecipient")
    commission_in_transfer_to_card_screen = ("id", "trastpay.uz:id/textViewCommission")
    overall_transfer_amount_in_transfer_screen = ("id", "trastpay.uz:id/textViewEnrolled")
    sent_money_confirm_screen = ("id", "trastpay.uz:id/textViewAmount")
    commission_confirm_screen = ("id", "trastpay.uz:id/textViewCommission")
    overall_money_confirm_screen = ("id", "trastpay.uz:id/textViewAllAmount")
    otp_screen_title = ("id", "trastpay.uz:id/textViewWellCome")
    otp_input_field = ("id", "trastpay.uz:id/edittext1")

    def is_transfer_to_card_screen_open(self):
        try:
            if self.is_visible(self.transfer_screen_title):
                return True
        except Exception:
            raise NoSuchElementException
        return False

    def is_confirm_transfer_screen_title(self):
        try:
            if self.is_visible(self.confirmation_screen_title):
                return True
        except Exception:
            raise NoSuchElementException
        return False

    def is_otp_screen_open(self):
        try:
            if self.is_visible(self.otp_screen_title):
                return True
        except Exception:
            raise NoSuchElementException
        return False

    def check_recipient_name_appeared_after_passing_card_number(self, recip_full_name_on_card):
        if recip_full_name_on_card in self.get_element_text(self.recipient_full_name_on_card):
            return True
        return False

    def check_all_data_appear_in_confirm_screen(self, recipient_details, sent_money, commission, overall_amount):
        if recipient_details in self.get_element_text(self.recipient_card_details_in_confirmation_screen):
            if sent_money in self.number_from_string(self.get_element_text(self.sent_money_confirm_screen)):
                if overall_amount in self.number_from_string(self.get_element_text(self.overall_money_confirm_screen)):
                    if commission in self.get_element_text(self.commission_confirm_screen):
                        return True
        return False

    def number_from_string(self, string):
        res = string.split(' ')
        res = res[0] + res[1]
        return res

    def get_appeared_commission_amount(self):
        print("Commission amount:  ", self.get_element_text(self.commission_in_transfer_to_card_screen).split(' ')[0])
        return self.get_element_text(self.commission_in_transfer_to_card_screen).split(' ')[0]

    def get_appeared_overall_amount(self, comission_amount):
        print("Commission amount: ", comission_amount)
        overall = self.get_element_text(self.overall_transfer_amount_in_transfer_screen).split(' ')
        print("OVERALL:       ->>>    ", overall[0], " ", overall[1])
        print("Length of calculated amount: ", len(overall), overall)
        if len(overall) == 2:
            if int(comission_amount) != 0:
                res = int(overall[0]) + int(comission_amount)
            else:
                res = int(overall[0])
        else:
            if int(comission_amount) != 0:
                res = int(overall[0] + overall[1]) + int(comission_amount)
            else:
                res = int(overall[0] + overall[1])
        res = '{:.2f}'.format(float(res))
        return str(res)

    def enter_recipient_card_number(self, card_numb):
        self.enter_data(self.recipient_card_input_field, card_numb)

    def enter_money_for_transferring(self, money_amount):
        self.enter_data(self.money_amount_input_field, money_amount)
        self.clear_text(self.money_amount_input_field)
        self.enter_data(self.money_amount_input_field, money_amount)

    def enter_otp(self, otp):
        self.enter_data(self.otp_input_field, otp)

    def click_on_sender_part(self):
        self.click(self.sender_part)

    def click_on_recipient_history_icon(self):
        self.click(self.recipient_from_history_icon)

    def click_on_transfer_to_card_icon_in_home(self):
        self.click(self.transfer_to_card_in_home_screen)

    def click_on_otkazish_button(self):
        self.click(self.otkazish_button)

    def select_card_by_last_4_number(self, last_four_numb):
        all_cards_numbers = self.get_elements(self.cards_number_ids)
        for card_numb in all_cards_numbers:
            if last_four_numb in card_numb.text:
                card_numb.click()
                break
            else:
                continue
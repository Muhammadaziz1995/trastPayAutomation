from screens.screen import Screen
from selenium.common import NoSuchElementException
import time


class MoneyExchangeScreen(Screen):
    money_exchange_screen_title = ("xpath", "//*[@text='Konversiya']")
    sender = ("id", "trastpay.uz:id/textViewSelectedSender")
    recipient = ("id", "trastpay.uz:id/textViewSelectedReceiver")
    manba_tanlang_title = ("xpath", "//*[@text='Manbani tanlang']")
    kartalar_title_name = ("xpath", "//*[@text='Kartalar']")
    trast_bank_name = ("xpath", "//*[@text='Trast Bank']")
    visa_card = ("xpath", "//*[contains(@text, '5309')]")
    recipient_card = ("xpath", "//*[contains(@text, \'{}\')]")
    selected_card_name = ("id", "trastpay.uz:id/textViewDescReceiver")
    recipient_card_account = ("id", "trastpay.uz:id/textViewReceiverBalance")
    input_for_uzs = ("id", "trastpay.uz:id/editTextUp")
    input_for_usd = ("id", "trastpay.uz:id/editTextDown")
    current_usd_rate = ("id", "trastpay.uz:id/textViewRate")
    final_usd_amount = ("id", "trastpay.uz:id/textViewReceiverAmount")
    send_btn = ("id", "trastpay.uz:id/btnContinue")
    confirm_screen_title = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                     "android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                     "/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/"
                                     "android.widget.LinearLayout/android.widget.TextView")
    swipe_icon = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                           "/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/"
                           "android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/"
                           "android.widget.LinearLayout/android.view.ViewGroup[1]/android.view.View[3]")
    """ Confirm screen """
    sender_card_number = '5802'
    """ Confirm screen """

    def is_money_exchange_screen_title_exist(self):
        if self.is_visible(self.money_exchange_screen_title):
            return True
        return False

    def is_manbani_tanlang_opened(self):
        if self.is_visible(self.manba_tanlang_title):
            if self.is_visible(self.kartalar_title_name):
                if self.is_visible(self.trast_bank_name):
                    return True
        return False

    def is_selected_card_info_appear(self, last_four_card_number):
        if last_four_card_number in self.get_element_text(self.selected_card_name):
            return True
        return False

    def is_recipient_account_USD_exists(self):
        if 'USD' in self.get_element_text(self.recipient_card_account):
            return True
        return False

    def is_final_usd_amount_exist(self):
        if '+ 1.00 USD' in self.get_element_text(self.final_usd_amount):
            return True
        return False

    def is_confirm_screen_open(self):
        if self.is_visible(self.confirm_screen_title):
            return True
        return False

    def click_on_recipient_part(self):
        self.click(self.recipient)

    def click_on_recipient_card_number(self, last_4_numb):
        print("Recipitient : ", self.recipient_card[1].format(last_4_numb))
        self.click_by_pasted_data(self.recipient_card, last_4_numb)

    def click_on_send_btn(self):
        self.click(self.send_btn)

    def click_on_swipe_icon(self):
        self.click(self.swipe_icon)

    def enter_money_amount(self, currency):
        if currency == 'uzs':
            if 'UZS dagi miqdor' in self.get_element_text(self.input_for_uzs):
                money = self.get_current_usd_rate()
                self.click(self.input_for_uzs)
                self.enter_data(self.input_for_uzs, money)
                self.clear_text(self.input_for_uzs)
                self.enter_data(self.input_for_uzs, money)
                self.hide_keyboard()
        else:
            if 'USD dagi miqdor' in self.get_element_text(self.input_for_usd):
                money = '1'
                self.enter_data(self.input_for_uzs, money)

    def get_current_usd_rate(self):
        usd_info = self.get_element_text(self.current_usd_rate).split(" ")
        usd_rate = usd_info[3] + usd_info[4]
        # print("usd rate: ", usd_rate)
        return usd_rate

    def get_current_usd_rate_text_for_cheque(self):
        usd_info = self.get_element_text(self.current_usd_rate).split(" ")
        usd_rate = usd_info[3] + " " + str(int(float(usd_info[4])))
        print("new usd rate: ", usd_rate)
        return usd_rate

    def get_sender_card_last_4_num(self):
        return self.sender_card_number


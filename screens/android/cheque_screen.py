from screens.screen import Screen
from selenium.common import NoSuchElementException
import datetime as d
import time


class ChequeScreen(Screen):

    """   ** P2P Transaction **   """
    success_img = ("id", "trastpay.uz:id/imgSuccess")
    muvaffaqqiyatli_cheque_title = ("id", "trastpay.uz:id/tvSuccess")
    cheque_details_list = ("id", "trastpay.uz:id/textViewValue")
    chek_transaction_details = ("id", "trastpay.uz:id/layoutTransactionDetails")
    to_home_screen_button = ("id", "trastpay.uz:id/btnContinue")
    """   ** P2P Transaction ends **   """

    def check_cheque_title(self):
        try:
            if self.is_visible(self.success_img) and self.is_visible(self.muvaffaqqiyatli_cheque_title):
                return True
        except Exception:
            raise NoSuchElementException
        return False

    def get_current_date(self):
        today = d.datetime.now()
        year = today.year
        month = today.month
        current_date = today.day
        res = "{}.{}.{}".format(current_date, month, year)
        cur_date = today.strftime("%y.%m.%d")
        return cur_date

    def check_cheque_details_in_last_cheque_screen(self, overall_amount, sent_summ, sender_info, commission,
                                                   recipient_info):
        date = self.get_current_date()
        matched_data = 0
        details = [overall_amount, sent_summ, date, sender_info, commission, recipient_info]
        cheque_details = self.get_elements(self.cheque_details_list)
        print("Elements length: ", len(cheque_details))
        for i in range(0, 6):
            if details[i] in cheque_details[i].text:
                matched_data += 1
                print(matched_data, " ", details[i], " ", cheque_details[i].text)

        if matched_data == len(cheque_details):
            print("All matched data : ", matched_data)
            return True
        return False

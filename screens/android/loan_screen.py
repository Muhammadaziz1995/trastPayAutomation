from screens.screen import Screen
from selenium.common import NoSuchElementException
import time


class LoanScreen(Screen):
    mening_mahsulotlarim = ("xpath", "//*[@text='Mening mahsulotlarim']")
    loans = ("xpath", "//*[@text='Kreditlar']")
    """  Loans screen  """
    loan_screen_title = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                               "android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/"
                               "android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/"
                               "android.widget.TextView")
    loan_name = ("id", "trastpay.uz:id/tvName")
    clickable_loan_name = ("id", "trastpay.uz:id/img")
    repay_icon = ("id", "trastpay.uz:id/img1")
    schedule_icon = ("id", "trastpay.uz:id/img3")
    details_icon = ("id", "trastpay.uz:id/img2")
    decreasing_loan_screen_title = ("id", "trastpay.uz:id/tvTittleToolbar")
    payment_type = ("id", "trastpay.uz:id/question")
    tolovlar_bottom_menu_title = ("id", "trastpay.uz:id/tvTittle")
    advanced_payment = ("id", "trastpay.uz:id/by_early")
    payment_amount_field = ("id", "trastpay.uz:id/et_amount")
    next_button = ("id", "trastpay.uz:id/nextButton")
    """  Loans screen ends  """

    def is_loans_screen_open(self):
        print("Kreditlar screen title : ", self.get_element_text(self.loan_screen_title))
        try:
            if "Kreditlar" in self.get_element_text(self.loan_screen_title):
                return True
        except NoSuchElementException as e:
            print(e.msg, "Error with ->> ", self.loan_screen_title)
        return False

    def is_loan_name_exist(self):
        try:
            if self.is_visible(self.loan_name):
                return True
        except Exception:
            raise NoSuchElementException
        return False

    def is_decreasing_loan_screen_open(self):
        try:
            if "Kreditni soʻndirish" in self.get_element_text(self.decreasing_loan_screen_title):
                return True
        except Exception:
            raise NoSuchElementException
        return False

    def is_tolovlar_bottom_menu_open(self):
        try:
            if "Toʻlov turi" in self.get_element_text(self.tolovlar_bottom_menu_title):
                return True
        except Exception:
            raise NoSuchElementException
        return False

    def enter_payment_amount(self, amount):
        self.enter_data(self.payment_amount_field, amount)

    def click_on_repay_icon(self):
        self.click(self.repay_icon)

    def click_on_mening_mahsulotlarim(self):
        self.click(self.mening_mahsulotlarim)

    def click_on_loans(self):
        self.click(self.loans)

    def click_on_microLoan_img(self):
        self.click(self.clickable_loan_name)

    def click_on_payment_type(self):
        self.click(self.payment_type)

    def click_on_advanced_payment(self):
        self.click(self.advanced_payment)

    def click_on_next_button(self):
        self.click(self.next_button)
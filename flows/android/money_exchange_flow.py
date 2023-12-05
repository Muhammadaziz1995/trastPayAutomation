from flows.android.android_base_flow import AndroidBaseFlow
import time


class MoneyExchangeFlow(AndroidBaseFlow):
    def __init__(self, driver, app_path):
        super().__init__(driver, app_path)
        self.driver = driver

    def check_money_exchange_from_uzs_to_usd_visa(self):
        pass

    def check_money_exchange_from_uzs_to_usd_master(self):
        pass

    def check_money_exchange_from_usd_to_uzs_visa(self):
        pass

    def check_money_transfer_from_usd_to_uzs_master(self):
        pass
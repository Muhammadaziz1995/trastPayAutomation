from flows.android.login_flow import LoginFlow
from flows.android.p2p_flow import P2PFlow
from flows.android.profile_flow import ProfileFlow
from flows.android.payments_flow import PaymentsFlow
from flows.android.loan_flow import LoanFlow
from flows.android.money_exchange_flow import MoneyExchangeFlow
import pytest


@pytest.fixture()
def create_login_flow_user_a(request, platform, emulator_1, app_path, get_screenshot_on_failed_case):
    if platform == "android":
        return LoginFlow(request.instance.driver_1, app_path)


@pytest.fixture()
def create_p2p_flow_user_a(request, platform, emulator_1, app_path, get_screenshot_on_failed_case):
    if platform == "android":
        return P2PFlow(request.instance.driver_1, app_path)


@pytest.fixture()
def create_profile_flow_user_a(request, platform, emulator_1, app_path, get_screenshot_on_failed_case):
    if platform == "android":
        return ProfileFlow(request.instance.driver_1, app_path)


@pytest.fixture()
def create_payments_flow_user_a(request, platform, emulator_1, app_path, get_screenshot_on_failed_case):
    if platform == "android":
        return PaymentsFlow(request.instance.driver_1, app_path)


@pytest.fixture()
def create_loan_flow_user_a(request, platform, emulator_1, app_path, get_screenshot_on_failed_case):
    if platform == "android":
        return LoanFlow(request.instance.driver_1, app_path)


@pytest.fixture()
def create_money_exchange_flow_user_a(request, platform, emulator_1, app_path, get_screenshot_on_failed_case):
    if platform == "android":
        return MoneyExchangeFlow(request.instance.driver_1, app_path)
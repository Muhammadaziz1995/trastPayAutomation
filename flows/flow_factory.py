from flows.android.login_flow import LoginFlow
from flows.android.p2p_flow import P2PFlow
import pytest


@pytest.fixture()
def create_login_flow_user_a(request, platform, emulator_1, app_path):
    if platform == "android":
        return LoginFlow(request.instance.driver_1, app_path)


@pytest.fixture()
def create_p2p_flow_user_a(request, platform, emulator_1, app_path):
    if platform == "android":
        return P2PFlow(request.instance.driver_1, app_path)
import allure
from allure_commons.types import AttachmentType


@allure.title("Registratsiyadan o'tishni testlash : data ['905439771', 19952913MXtuit*]")
class TestSuitLogin:
    def test_case_login(self, create_login_flow_user_a):
        user_a_flow = create_login_flow_user_a
        assert user_a_flow.check_login("905439771", "19952913MXtuit*")
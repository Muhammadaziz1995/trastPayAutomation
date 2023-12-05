import allure
from allure_commons.types import AttachmentType


@allure.title("Application Belgilangan vaqtda lock bo'lishini profile orqali tekshirish")
class TestSuitProfile:
    def test_profile_flow(self, create_profile_flow_user_a):
        user_a = create_profile_flow_user_a
        assert user_a.check_app_lock_time()
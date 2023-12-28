import allure
from allure_commons.types import AttachmentType


class TestSuitLoan:
    def test_suit_loan(self, create_loan_flow_user_a):
        user_a = create_loan_flow_user_a
        assert user_a.check_advanced_repayment('Bank', '1000', '5802', '0', '47008827', '1 000')
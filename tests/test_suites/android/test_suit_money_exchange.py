class TestSuitMoneyExchange:
    def test_case_money_exchange_uzs_to_usd_visa(self, create_money_exchange_flow_user_a):
        user_a = create_money_exchange_flow_user_a
        # assert user_a.check_money_exchange_from_uzs_to_usd_visa('5309', 'uzs')
        assert user_a.check_money_exchange_from_usd_to_uzs_visa('5309', 'uzs')
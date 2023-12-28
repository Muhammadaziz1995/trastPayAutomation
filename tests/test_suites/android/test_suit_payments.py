class TestSuitPayments:
    def test_payments(self, create_payments_flow_user_a):
        user_a = create_payments_flow_user_a
        assert user_a.pay_to_mobile_beeline("905439771", "500", "Mobil Aloqa", "Beeline", "5802", "0")
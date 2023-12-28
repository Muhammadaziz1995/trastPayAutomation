class TestSuitP2PH2U:
    # @pytest.mark.usefixtures('create_p2p_flow_user_a')
    def test_case_p2p_h2u(self, create_p2p_flow_user_a):
        user_a_flow = create_p2p_flow_user_a
        assert user_a_flow.check_p2p_humo_to_uzcard("0118", "8600140255564529", "500", "4529", "XOLIQBERDIYEV MUHAMMADAZIZ")
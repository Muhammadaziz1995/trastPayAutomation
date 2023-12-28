class TestSuitP2PH2H:
    # @pytest.mark.usefixtures('create_p2p_flow_user_a')
    def test_case_p2p_h2h(self, create_p2p_flow_user_a):
        user_a_flow = create_p2p_flow_user_a

        assert user_a_flow.check_p2p_humo_to_humo_from_home_screen("0118", "9860200101864805", "500", "4805",
                                                                   "M XOLIQBERDIYEV", "XOLIQBERDIYEV M")
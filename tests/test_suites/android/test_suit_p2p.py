import pytest


class TestSuitP2P:
    # @pytest.mark.usefixtures('create_p2p_flow_user_a')
    def p2p(self, create_p2p_flow_user_a):
        user_a_flow = create_p2p_flow_user_a

        assert user_a_flow.check_p2p_humo_to_humo_from_home_screen("0118", "9860200101864805", "500", "4805",
                                                                   "M XOLIQBERDIYEV", "XOLIQBERDIYEV M")
        assert user_a_flow.check_p2p_humo_to_uzcard("0118", "8600140255564529", "500", "4529", "XOLIQBERDIYEV MUHAMMADAZIZ")
        assert user_a_flow.check_p2p_uzcard_own_to_uzcard_other("7163", "8600140255564529", "XOLIQBERDIYEV MUHAMMADAZIZ",
                                                                "500")
        assert user_a_flow.check_p2p_uzcard_to_humo("7163", "9860180101645802", "MUKHAMMADAZIZ K", "500")
        assert user_a_flow.check_p2p_humo_to_wallet("0118", "500", "Sum account")

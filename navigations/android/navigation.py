from screens.screen import Screen


class NavigationAndroid(Screen):
    def __init__(self, android_base_flow):
        super().__init__(android_base_flow.driver)
        self.screens = android_base_flow

    def jump_to_verification_screen(self, email, sign_up):
        self.screens.signIn_screen.enter_email_to_email_field(email, sign_up)
        assert self.screens.verification_screen.ver_screen_is_opened()

    def jump_to_cards_screen_by_friends_email(self, email, sign_up, pl_ver):
        self.jump_to_verification_screen(email, sign_up) # sign_up -> yes
        self.screens.verification_screen.receive_link2(pl_ver)
        assert self.screens.cards_screen.is_cards_screen_opened()


    def jump_to_verification_screen_new_user(self, email, sign_up):
        self.screens.signIn_screen.enter_email_to_email_field(email, sign_up)
        assert self.screens.verification_screen.ver_screen_is_opened()

    def jump_to_profile_screen_unsigned_user(self, is_signed, pl_ver):
        self.screens.verification_screen.receive_link(is_signed, pl_ver)
        assert self.screens.profile_screen.is_profile_screen_opened()

    def jump_to_cards_screen_signed_user(self, email, is_sign_up, is_signed, platform_version):
        self.jump_to_verification_screen(email, is_sign_up)
        self.screens.verification_screen.receive_link(is_signed, platform_version)
        assert self.screens.cards_screen.is_cards_screen_opened()

    def jump_to_cards_via_profile_screen(self, first_name, last_name):
        self.screens.profile_screen.fill_fullname(first_name, last_name)
        assert self.screens.cards_screen.is_cards_screen_opened()

    def jump_to_connect_screen(self):
        self.screens.cards_screen.tap_on_connect_icon()
        assert self.screens.cards_screen.is_connect_screen_opened()

    def jump_to_own_profile_screen(self):
        self.screens.cards_screen.tap_on_profile_icon()
        assert self.screens.myContactID_screen.is_myContactId_opened()

    def jump_to_gmail_app(self, plf_v):
        self.screens.verification_screen.open_gmail(plf_v)

    def jump_to_settings_screen(self):
        self.screens.myContactID_screen.tap_on_settings_icon()
        assert self.screens.myContactID_screen.is_settings_title_exist()

import re

import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


class TestLogin:
    @pytest.fixture(autouse=True)
    def login_page(self, page: Page) -> LoginPage:
        self.login_page = LoginPage(page)
        self.login_page.open()
        return self.login_page

    def test_user_can_log_in_and_out(self, page: Page) -> None:
        self.login_page.login("tomsmith", "SuperSecretPassword!")

        expect(page).to_have_url(re.compile(r"/secure$"))
        expect(self.login_page.flash).to_contain_text("You logged into a secure area!")

        self.login_page.logout()
        expect(self.login_page.flash).to_contain_text("You logged out of the secure area!")

    @pytest.mark.parametrize(
        ("username", "password", "message"),
        [
            ("wrong-user", "SuperSecretPassword!", "Your username is invalid!"),
            ("tomsmith", "wrong-password", "Your password is invalid!"),
        ],
    )
    def test_rejects_invalid_credentials(
        self, username: str, password: str, message: str
    ) -> None:
        self.login_page.login(username, password)

        expect(self.login_page.flash).to_contain_text(message)

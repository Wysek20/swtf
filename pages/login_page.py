from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.username = page.get_by_label("Username")
        self.password = page.get_by_label("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.logout_link = page.get_by_role("link", name="Logout")
        self.flash = page.locator("#flash")

    def open(self) -> None:
        self.page.goto("/login")

    def login(self, username: str, password: str) -> None:
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def logout(self) -> None:
        self.logout_link.click()

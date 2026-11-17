from playwright.sync_api import Page, expect


def test_homepage_lists_examples(page: Page) -> None:
    page.goto("/")

    expect(page.get_by_role("heading", name="Welcome to the-internet")).to_be_visible()
    expect(page.get_by_role("link", name="Form Authentication")).to_be_visible()

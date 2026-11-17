from playwright.sync_api import Page, expect


def test_selecting_an_option(page: Page) -> None:
    page.goto("/dropdown")
    dropdown = page.locator("#dropdown")

    dropdown.select_option(label="Option 2")

    expect(dropdown).to_have_value("2")

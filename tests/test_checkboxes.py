from playwright.sync_api import Page, expect


def test_checkboxes_can_be_changed(page: Page) -> None:
    page.goto("/checkboxes")
    checkboxes = page.get_by_role("checkbox")
    first_checkbox = checkboxes.nth(0)
    second_checkbox = checkboxes.nth(1)

    expect(first_checkbox).not_to_be_checked()
    expect(second_checkbox).to_be_checked()

    first_checkbox.check()
    second_checkbox.uncheck()

    expect(first_checkbox).to_be_checked()
    expect(second_checkbox).not_to_be_checked()

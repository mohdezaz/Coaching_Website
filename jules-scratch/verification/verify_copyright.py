from playwright.sync_api import sync_playwright, Page, expect
import os

def run(page: Page):
    # Get the absolute path to the HTML file
    file_path = os.path.abspath('index.html')
    # Use file:// protocol to open the local file
    page.goto(f'file://{file_path}')

    # Find the footer
    footer = page.locator(".site-footer")

    # Scroll to the footer to ensure it's in view
    footer.scroll_into_view_if_needed()

    # Wait for the element to be visible
    expect(footer).to_be_visible()

    # Take a screenshot of the footer
    footer.screenshot(path='jules-scratch/verification/verification.png')


if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        run(page)
        browser.close()
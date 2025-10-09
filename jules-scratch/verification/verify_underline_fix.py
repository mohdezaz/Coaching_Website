import os
from playwright.sync_api import sync_playwright, expect

def run_verification():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get the absolute path to the index.html file
        current_dir = os.getcwd()
        file_path = f"file://{os.path.join(current_dir, 'index.html')}"

        page.goto(file_path)

        # Hover over the "Courses" dropdown link
        courses_link = page.locator('a.dropbtn:has-text("Courses")')
        courses_link.hover()

        # Wait for any potential animations to complete
        page.wait_for_timeout(500)

        # Take a screenshot of the navigation bar
        screenshot_path = "jules-scratch/verification/no_underline_verification.png"
        page.locator('header').screenshot(path=screenshot_path)

        browser.close()
        print(f"Screenshot saved to {screenshot_path}")

if __name__ == "__main__":
    run_verification()
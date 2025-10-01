from playwright.sync_api import sync_playwright
import os

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    # Get the absolute path to the index.html file
    base_path = os.path.abspath('.')
    index_path = f'file://{os.path.join(base_path, "index.html")}'
    page.goto(index_path)
    page.wait_for_timeout(1000) # Wait for animations

    # 1. Test Mobile View
    page.set_viewport_size({"width": 375, "height": 667})
    page.screenshot(path='jules-scratch/verification/mobile_view.png')

    # 2. Test Hamburger Menu
    hamburger = page.locator('.hamburger-menu')
    hamburger.click()
    page.wait_for_timeout(500) # Wait for overlay transition
    page.screenshot(path='jules-scratch/verification/mobile_nav_open.png')

    close_btn = page.locator('.close-btn')
    close_btn.click()
    page.wait_for_timeout(500)

    # 3. Test Tablet View
    page.set_viewport_size({"width": 768, "height": 1024})
    page.screenshot(path='jules-scratch/verification/tablet_view.png')

    # 4. Test Desktop View
    page.set_viewport_size({"width": 1280, "height": 800})
    page.screenshot(path='jules-scratch/verification/desktop_view.png')

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
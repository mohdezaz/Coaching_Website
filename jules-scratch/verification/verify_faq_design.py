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

    # 1. Scroll to the FAQ section and take a screenshot
    faq_section = page.locator('.faq-section')
    faq_section.scroll_into_view_if_needed()
    page.wait_for_timeout(500) # Wait for scroll to settle
    page.screenshot(path='jules-scratch/verification/faq_section.png')

    # 2. Click the first accordion and take a screenshot of the open state
    first_accordion = page.locator('.accordion').first
    first_accordion.click()
    page.wait_for_timeout(500) # Wait for accordion animation
    page.screenshot(path='jules-scratch/verification/faq_section_open.png')

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
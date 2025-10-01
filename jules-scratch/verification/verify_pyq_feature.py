from playwright.sync_api import sync_playwright
import os

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    # Get the absolute path to the HTML files
    base_path = os.path.abspath('.')

    # 1. Verify pyqs.html
    pyqs_path = f'file://{os.path.join(base_path, "pyqs.html")}'
    page.goto(pyqs_path)
    page.wait_for_timeout(1000)  # Wait for animations
    page.screenshot(path='jules-scratch/verification/pyqs_page.png')

    # 2. Verify a PYQ content page (e.g., NEET Physics)
    neet_physics_link = page.locator('a[href="pyq-content/neet/physics.html"]')
    neet_physics_link.click()
    page.wait_for_load_state()
    page.wait_for_timeout(1000)  # Wait for animations
    page.screenshot(path='jules-scratch/verification/pyq_content_page.png')

    # 3. Verify index.html for the new "Featured PYQs" section
    index_path = f'file://{os.path.join(base_path, "index.html")}'
    page.goto(index_path)
    # Scroll to the new section to make sure it's in view
    featured_pyqs_section = page.locator('.featured-pyqs-section')
    featured_pyqs_section.scroll_into_view_if_needed()
    page.wait_for_timeout(1000)  # Wait for animations
    page.screenshot(path='jules-scratch/verification/index_page_with_pyqs.png')

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
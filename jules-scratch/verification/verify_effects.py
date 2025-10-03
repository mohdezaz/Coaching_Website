from playwright.sync_api import sync_playwright
import os

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    # Get absolute paths
    index_path = "file://" + os.path.abspath("index.html")
    our_team_path = "file://" + os.path.abspath("our-team.html")
    contact_path = "file://" + os.path.abspath("contact.html")
    about_path = "file://" + os.path.abspath("about.html")
    courses_path = "file://" + os.path.abspath("courses.html")

    # 1. Verify nav link hover
    page.goto(index_path)
    page.wait_for_load_state()
    page.hover("nav ul li a[href='about.html']")
    page.screenshot(path="jules-scratch/verification/nav-hover.png")

    # 2. Verify button hover
    page.goto(index_path)
    page.wait_for_load_state()
    page.hover("a.cta-button:has-text('Explore Our Courses')")
    page.screenshot(path="jules-scratch/verification/button-hover.png")

    # 3. Verify card hover
    page.goto(our_team_path)
    page.wait_for_load_state()
    page.hover(".faculty-card")
    page.screenshot(path="jules-scratch/verification/card-hover.png")

    # 4. Verify icon hover
    page.goto(contact_path)
    page.wait_for_load_state()
    page.locator(".contact-section").scroll_into_view_if_needed()
    page.hover(".contact-item")
    page.screenshot(path="jules-scratch/verification/icon-hover.png")

    # 5. Verify dropdown animation
    page.goto(courses_path)
    page.wait_for_load_state()
    page.hover(".dropdown")
    page.wait_for_timeout(500) # Wait for animation
    page.screenshot(path="jules-scratch/verification/dropdown-hover.png")

    # 6. Verify philosophy card icon hover
    page.goto(about_path)
    page.wait_for_load_state()
    page.locator(".our-philosophy").scroll_into_view_if_needed()
    page.hover(".philosophy-card")
    page.screenshot(path="jules-scratch/verification/philosophy-card-hover.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
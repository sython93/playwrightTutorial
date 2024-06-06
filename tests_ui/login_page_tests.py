from playwright.sync_api import Playwright, sync_playwright, expect
from pom.home_page_elements import HomePage
from pom.login_page_elements import LoginPage

# Log in & navigate to subdomain landing page
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = browser.new_page()
    home_page = HomePage(page)
    login_page = LoginPage(page)
    page.set_viewport_size({"width": 1500, "height": 1080})
    page.goto("https://sam.clarussoftware.co.uk/login")
    page.pause()
    expect(login_page.email).to_be_visible()
    page.get_by_label("email").click()
    page.get_by_label("email").fill("sam.stringer@clarussoftware.co.uk")
    page.get_by_label("password").click()
    page.get_by_label("password").fill("Ssasrl30132543!")
    page.get_by_role("button", name="Sign In").click()
    expect(login_page.email).to_be_hidden()
    expect(login_page.password).to_be_hidden()
    expect(login_page.sign_in_button).to_be_hidden()
    expect(home_page.stock_dropdown).to_be_visible()
    expect(home_page.dynamic_toggle).to_be_visible()
    expect(home_page.ctrlk_button).to_be_visible()



    print("Log in & Landing page test passed")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

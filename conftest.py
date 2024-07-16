import playwright


def page(playwright: playwright, scope="module"):
    app_data_path = os.getenv("LOCALAPPDATA")
    chromium_path = "ms-playwright\\chromium-1028\\chrome-win"
    chromium_path = os.path.join(app_data_path, chromium_path)
    chrome = playwright.chromium\
        .launch_persistent_context(chromium_path, headless=False, args=["--start-maximised"], no_viewport=True)
    page = chrome.new_page()
    return page

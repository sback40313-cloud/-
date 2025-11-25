from playwright.sync_api import Playwright, sync_playwright, expect
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()
    page.goto("https://swag.live/?lang=zh-TW")

    page.get_by_role("button", name="免費註冊/登入").click()
    page.get_by_role("button", name="點此登入").click()
    page.get_by_role("button", name="帳號密碼登入").click()
    page.get_by_role("textbox", name="用户名稱").click()
    page.get_by_role("textbox", name="用户名稱").fill("interviewuser1234")
    page.get_by_role("textbox", name="密碼").click()
    page.get_by_role("textbox", name="密碼").fill("newinter12345")

    page.locator("#modal-root").get_by_role("button", name="登入", exact=True).click()
    page.get_by_role("button", name="選單").click()
    page.get_by_role("link", name="大頭貼 I @ interviewuser1234 more").click()
    # ---------------------
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)
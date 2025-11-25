import re
import time
from time import sleep
from playwright.sync_api import Playwright, sync_playwright, expect
def run(playwright: Playwright) -> None:
    browser = None
    context = None
    try:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(ignore_https_errors=True)
        page = context.new_page()
        # 登入流程
        page.goto("https://swag.live/?lang=zh-TW")
        time.sleep(3)
        page.get_by_role("button", name="免費註冊/登入").click()
        page.get_by_role("button", name="點此登入").click()
        page.get_by_role("button", name="帳號密碼登入").click()
        page.get_by_role("textbox", name="用户名稱").fill("interviewuser1234")
        page.get_by_role("textbox", name="密碼").fill("newinter1234")
        time.sleep(3)
        page.locator("#modal-root").get_by_role("button", name="登入", exact=True).click()
        page.get_by_role("button", name="選單").click()
        page.get_by_role("link", name="大頭貼 I @ interviewuser1234 more").click()
        print(":白色勾勾: 登入流程已完成")
    except Exception as e:
        print(":x: 登入流程失敗:", e)
    finally:
        if context:
            context.close()
        if browser:
            browser.close()
with sync_playwright() as playwright:
    run(playwright)
from playwright.sync_api import Playwright, sync_playwright, expect
import os
import config
from email_functions import send_email
from email_functions import send_email_thru_outlook
from email_functions import send_final_email_thru_outlook

from cryptography.fernet import Fernet

def decrypt_message(encrypted_message):
    key = config.secret["key"] # replace with secret key after deployment
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()

import os
import signal

def exit_parent_process():
    parent_pid = os.getppid()
    os.kill(parent_pid, signal.SIGTERM)

def run(playwright: Playwright) -> None:

    username = config.login["username"]
    password = decrypt_message(config.login["password"])
    url = config.login["url"]
    download_folder = config.var["download_folder"]

    browser = playwright.chromium.launch(headless=False, slow_mo=2000)

    context = browser.new_context()
    
    page = context.new_page()
    page.goto(url)
    page.get_by_test_id("").click()

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)


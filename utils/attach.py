import allure
from allure_commons.types import AttachmentType

# Скриншоты
def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')

# логи
def add_logs(browser):
    try:
        devtools = browser.driver.get_devtools()
        logs = devtools.get_logs()
        if logs:
            log_text = "\n".join(str(log) for log in logs)
            allure.attach(log_text, name="devtools_logs", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        allure.attach(f"DevTools error: {str(e)}", name="devtools_error", attachment_type=allure.attachment_type.TEXT)

# html-код страницы
def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')
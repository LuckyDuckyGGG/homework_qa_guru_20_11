import allure
from allure_commons.types import AttachmentType

# Скриншоты
def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')

# логи
def add_logs(browser):
    try:
        logs = browser.driver.get_log("browser")  # или "performance"
        if logs:
            log_text = "\n".join(str(log) for log in logs)
            allure.attach(log_text, name="browser_logs", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach("No browser logs available", name="browser_logs", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        allure.attach(f"Failed to get logs: {str(e)}", name="log_error", attachment_type=allure.attachment_type.TEXT)

# html-код страницы
def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')
import time

from webdriver_wrapper import WebDriverWrapper


def scraper_handler(event, context):
    driver = WebDriverWrapper()

    driver.get_url(event['url'])

    source = driver.get_html()

    driver.close()

    return source

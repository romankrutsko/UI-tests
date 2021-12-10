from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class Tests(TestCase):
    def test_search(self):
        search_request = 'rtx 3080'
        url = 'https://gamehall.com.ua/'

        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.implicitly_wait(10)

        browser.get(url)

        browser.find_element_by_css_selector('[id="s-529"]').send_keys(search_request, Keys.ENTER)

        actualResult = browser.find_element_by_css_selector('[class="heading-title page-title entry-title "]').text

        expectedResult = search_request

        assert expectedResult in actualResult
        browser.close()

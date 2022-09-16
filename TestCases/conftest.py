import pytest
from selenium import webdriver
driver = None
import configparser
config = configparser.ConfigParser()
config.read("utilities/input.properties")


@pytest.fixture
def setup(request):
    request.cls.driver = webdriver.Chrome("Driver\\chromedriver.exe")
    request.cls.driver.get(config.get("url", "base_url"))
    yield
    request.cls.driver.quit()
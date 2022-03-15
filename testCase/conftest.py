from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome("C://Users/TUAN/PycharmProjects/pythonProject6/drivers/chromedriver.exe")
    return driver
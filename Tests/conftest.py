
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def chrome_setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    request.cls.driver = driver
    print("Lounching Chrome......")
    driver.maximize_window()
    yield
    driver.quit()


@pytest.fixture(scope="class")
def edge_setup(request):
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    request.cls.driver = driver
    print("Lounching Edge......")
    driver.maximize_window()
    yield
    driver.quit()
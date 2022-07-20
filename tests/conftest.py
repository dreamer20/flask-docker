import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--host", action="store", default="0.0.0.0", help="Set host to selenium test"
    )
    parser.addoption(
        "--port", action="store", default="4444", help="Set port to selenium test"
    )


@pytest.fixture
def host(request):
    return request.config.getoption("--host")


@pytest.fixture
def port(request):
    return request.config.getoption("--port")

from selenium import webdriver
import pytest
from pytest_metadata.plugin import metadata_key


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("launching firefox browser.......")
    else:
        driver = webdriver.Edge()
        print("Launching default browser edge.........")
    return driver


def pytest_addoption(parser):  # this will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return the browser value to setup method
    return request.config.getoption("--browser")


###########pytest html report##############
# it is a hook for adding environment info to HTML report

def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'nop Commerce'
    config.stash[metadata_key]['Module Name'] = 'Customers'
    config.stash[metadata_key]['Tester'] = 'Pavan'


# Remove or modify environment info in HTML report
def pytest_metadata(metadata):
    # Remove specific entries from the metadata dictionary
    if "JAVA HOME" in metadata:
        metadata.pop("JAVA HOME")
    if "Plugins" in metadata:
        metadata.pop("Plugins")

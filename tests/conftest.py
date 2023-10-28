import pytest
from selene import browser
from selenium import webdriver


DESKTOP_RESOLUTIONS = [
    [1920, 1080],
    [1600, 1200]
]

MOBILE_RESOLUTIONS = [
    [360, 800],
    [412, 915]
]

RESOLUTIONS = DESKTOP_RESOLUTIONS + MOBILE_RESOLUTIONS


@pytest.fixture(scope="function")
def browser_desktop():
    browser.config.driver = webdriver.Chrome()
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()


@pytest.fixture(scope="function")
def browser_mobile():
    browser.config.driver = webdriver.Chrome()
    browser.config.window_width = 360
    browser.config.window_height = 800

    yield

    browser.quit()


@pytest.fixture(params=RESOLUTIONS)
def browser_setup(request):
    browser.config.driver = webdriver.Chrome()
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    yield

    browser.quit()


only_desktop = pytest.mark.parametrize('browser_setup',
                                       DESKTOP_RESOLUTIONS,
                                       indirect=True)

only_mobile = pytest.mark.parametrize('browser_setup',
                                      MOBILE_RESOLUTIONS,
                                      indirect=True)

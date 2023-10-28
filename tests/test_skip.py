"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser

from tests.models.github_home_page import GitHubHomePage
from tests.conftest import MOBILE_RESOLUTIONS, DESKTOP_RESOLUTIONS


def resolution():
    return [browser.config.window_width,
            browser.config.window_height]


def test_github_desktop(browser_setup):
    if resolution() not in DESKTOP_RESOLUTIONS:
        pytest.skip()

    page = GitHubHomePage()
    page.open()
    page.sign_in_desktop()

    page.should_show_auth_form()


def test_github_mobile(browser_setup):
    if resolution() not in MOBILE_RESOLUTIONS:
        pytest.skip()

    page = GitHubHomePage()
    page.open()
    page.sign_in_mobile()

    page.should_show_auth_form()

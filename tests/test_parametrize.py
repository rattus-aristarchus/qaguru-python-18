"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
from tests.conftest import only_desktop, only_mobile
from tests.models.github_home_page import GitHubHomePage


@only_desktop
def test_github_desktop(browser_setup):
    page = GitHubHomePage()
    page.open()
    page.sign_in_desktop()

    page.should_show_auth_form()


@only_mobile
def test_github_mobile(browser_setup):
    page = GitHubHomePage()
    page.open()
    page.sign_in_mobile()

    page.should_show_auth_form()

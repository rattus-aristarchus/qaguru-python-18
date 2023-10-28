"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""

from tests.models.github_home_page import GitHubHomePage


def test_github_desktop(browser_desktop):
    page = GitHubHomePage()
    page.open()
    page.sign_in_desktop()

    page.should_show_auth_form()


def test_github_mobile(browser_mobile):
    page = GitHubHomePage()
    page.open()
    page.sign_in_mobile()

    page.should_show_auth_form()

from selene import browser, have, command, be


class GitHubHomePage:

    def open(self):
        browser.open("https://github.com")
        browser.all("[id^=google_ads][id$=container__]").with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def sign_in_desktop(self):
        #browser.element('.HeaderMenu-link--sign-in').click()

        browser.element('[class*=--sign-in]').click()

    def sign_in_mobile(self):
        #browser.element('.flex-order-2 .Button-label').click()
        #browser.element('.HeaderMenu-link--sign-in').click()

        browser.element('.Button--link').click()
        browser.element('[class*=--sign-in]').click()

    def should_show_auth_form(self):
        browser.element('.auth-form-body').should(be.visible)

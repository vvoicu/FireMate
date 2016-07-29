from tools.WebdriverBase import WebdriverBase


usernameInputLocator = "#username"
userpassInputLocator = "#password"
loginButtonLocator = "#submit"

class LoginPage(WebdriverBase):

    def input_user_name(self, userName):
        userInput = WebdriverBase().locate_element_by_css_selector(usernameInputLocator)
        userInput.send_keys(userName)

    def input_user_pass(self, userPass):
        userInput = WebdriverBase().locate_element_by_css_selector(userpassInputLocator)
        userInput.send_keys(userPass)

    def click_login_button(self):
        loginButton = WebdriverBase().locate_element_by_css_selector(loginButtonLocator)
        loginButton.click()
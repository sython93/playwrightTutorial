

class LoginPage:

    def __init__(self, page):
        self.sign_in_button = page.get_by_role("button", name="Sign In")
        self.email = page.get_by_label("email")
        self.password = page.get_by_label("password")
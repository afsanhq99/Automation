def test_positive_login(login_page):
    login_page.open()
    login_page.login("student", "Password123")
    assert login_page.is_logged_in()
    assert login_page.is_logout_button_displayed()


def test_negative_username(login_page):
    login_page.open()
    login_page.login("studentt", "Password1234")
    assert login_page.is_error_message_displayed()
    assert login_page.get_error_message_text() == "Your username is invalid!"


def test_negative_password(login_page):
    login_page.open()
    login_page.login("student", "Password12344")
    assert login_page.is_error_message_displayed()
    assert login_page.get_error_message_text() == "Your password is invalid!"
